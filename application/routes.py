from application import app, db, api
from application.models import vocabulary, user
from flask import render_template, json, Response, flash, redirect, jsonify,request, session,url_for
from application.forms import LoginForm
from flask_restplus import Resource

    
data = [{'STT': 'HSK1_1_1', 'TIẾNG VIỆT ': 'Chào bạn', 'PHIÊN ÂM': 'nǐ hǎo', 'TIẾNG TRUNG': '你好', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': 'Chào bạn Số đếm lượng ít: Chào anh, chào chị,…'}, {'STT': 'HSK1_1_2', 'TIẾNG VIỆT ': 'Chào ông', 'PHIÊN ÂM': 'nín hǎo', 'TIẾNG TRUNG': '您好', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': 'Chào người lớn tuổi Chào ông, chào cô,…'}, {'STT': 'HSK1_1_3', 'TIẾNG VIỆT ': 'Chào các ban', 'PHIÊN ÂM': 'nǐ men hǎo', 'TIẾNG TRUNG': '你们好', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': 'Chào nhiều người: Chào các bạn, chào các anh,…'}, {'STT': 'HSK1_1_4', 'TIẾNG VIỆT ': 'Xin lỗi', 'PHIÊN ÂM': 'duì bu qī', 'TIẾNG TRUNG': '对不起', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_5', 'TIẾNG VIỆT ': 'Không sao đâu, không có vấn đề gì', 'PHIÊN ÂM': 'méi guān xi', 'TIẾNG TRUNG': '没关系', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_6', 'TIẾNG VIỆT ': 'Mẹ', 'PHIÊN ÂM': 'mā', 'TIẾNG TRUNG': '吗', 'PHÂN LOẠI': 'Gia đình', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_7', 'TIẾNG VIỆT ': 'Cây gai', 'PHIÊN ÂM': 'má', 'TIẾNG TRUNG': '麻', 'PHÂN LOẠI': 'Thực vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_8', 'TIẾNG VIỆT ': 'Con ngựa', 'PHIÊN ÂM': 'mǎ', 'TIẾNG TRUNG': '马', 'PHÂN LOẠI': 'Động vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_9', 'TIẾNG VIỆT ': 'Mắng', 'PHIÊN ÂM': 'mà', 'TIẾNG TRUNG': '骂', 'PHÂN LOẠI': 'Hành động', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_10', 'TIẾNG VIỆT ': 'Số đếm 5', 'PHIÊN ÂM': 'wǔ', 'TIẾNG TRUNG': '五', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_11', 'TIẾNG VIỆT ': 'Con cá', 'PHIÊN ÂM': 'yú', 'TIẾNG TRUNG': '鱼', 'PHÂN LOẠI': 'Động vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_12', 'TIẾNG VIỆT ': 'Tai', 'PHIÊN ÂM': 'ěr', 'TIẾNG TRUNG': '耳', 'PHÂN LOẠI': 'Bộ phận con người', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_13', 'TIẾNG VIỆT ': 'Bút', 'PHIÊN ÂM': 'bǐ', 'TIẾNG TRUNG': '笔', 'PHÂN LOẠI': 'Đồ vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_14', 'TIẾNG VIỆT ': 'Con mèo', 'PHIÊN ÂM': 'māo', 'TIẾNG TRUNG': '猫', 'PHÂN LOẠI': 'Động vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_15', 'TIẾNG VIỆT ': 'Hòn đảo', 'PHIÊN ÂM': 'dǎo', 'TIẾNG TRUNG': '岛', 'PHÂN LOẠI': 'Địa điểm', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_16', 'TIẾNG VIỆT ': 'Bông hoa', 'PHIÊN ÂM': 'huā', 'TIẾNG TRUNG': '华', 'PHÂN LOẠI': 'Thực vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_17', 'TIẾNG VIỆT ': 'Con gà', 'PHIÊN ÂM': 'jī', 'TIẾNG TRUNG': '鸡', 'PHÂN LOẠI': 'Động vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_18', 'TIẾNG VIỆT ': 'Số đếm 7', 'PHIÊN ÂM': 'qī', 'TIẾNG TRUNG': '七', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_19', 'TIẾNG VIỆT ': 'Giày', 'PHIÊN ÂM': 'xié', 'TIẾNG TRUNG': '鞋', 'PHÂN LOẠI': 'Đồ vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_20', 'TIẾNG VIỆT ': 'Tuyết', 'PHIÊN ÂM': 'xuě', 'TIẾNG TRUNG': '雪', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_21', 'TIẾNG VIỆT ': 'Cà phê', 'PHIÊN ÂM': 'kā fēi', 'TIẾNG TRUNG': '咖啡', 'PHÂN LOẠI': 'Thứ uống', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_22', 'TIẾNG VIỆT ': 'Cola', 'PHIÊN ÂM': 'kě lè', 'TIẾNG TRUNG': '可乐', 'PHÂN LOẠI': 'Thức uống', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_23', 'TIẾNG VIỆT ': 'Máy bay', 'PHIÊN ÂM': 'fēi jī', 'TIẾNG TRUNG': '飞机', 'PHÂN LOẠI': 'Phương tiện vận tải', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_24', 'TIẾNG VIỆT ': 'Tai nghe', 'PHIÊN ÂM': 'ěr jī', 'TIẾNG TRUNG': '耳机', 'PHÂN LOẠI': 'Đồ vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_25', 'TIẾNG VIỆT ': 'Vào học đi', 'PHIÊN ÂM': 'shàng kè', 'TIẾNG TRUNG': '上课', 'PHÂN LOẠI': 'Mẫu câu thường dùng trong lớp học', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_26', 'TIẾNG VIỆT ': 'Đã hết giờ học rồi', 'PHIÊN ÂM': 'xià kè', 'TIẾNG TRUNG': '下课', 'PHÂN LOẠI': 'Mẫu câu thường dùng trong lớp học', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_27', 'TIẾNG VIỆT ': 'Nghỉ giải lao nhé', 'PHIÊN ÂM': 'xiàn zài xiù xi', 'TIẾNG TRUNG': '现在 休息', 'PHÂN LOẠI': 'Mẫu câu thường dùng trong lớp học', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_28', 'TIẾNG VIỆT ': 'Hãy nhìn lên bảng', 'PHIÊN ÂM': 'kàn hěi bǎn', 'TIẾNG TRUNG': '看 黑板', 'PHÂN LOẠI': 'Mẫu câu thường dùng trong lớp học', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_29', 'TIẾNG VIỆT ': 'Hãy đọc theo tôi', 'PHIÊN ÂM': 'gēn wǒ dú', 'TIẾNG TRUNG': '跟我读', 'PHÂN LOẠI': 'Mẫu câu thường dùng trong lớp học', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_30', 'TIẾNG VIỆT ': 'Số đếm 2', 'PHIÊN ÂM': 'èr', 'TIẾNG TRUNG': '二', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_31', 'TIẾNG VIỆT ': 'Công việc', 'PHIÊN ÂM': 'gōng', 'TIẾNG TRUNG': '工', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_32', 'TIẾNG VIỆT ': 'Số đếm 10', 'PHIÊN ÂM': 'shí', 'TIẾNG TRUNG': '十', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_33', 'TIẾNG VIỆT ': 'Người', 'PHIÊN ÂM': 'rén', 'TIẾNG TRUNG': '人', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_34', 'TIẾNG VIỆT ': 'Số đếm 8', 'PHIÊN ÂM': 'bā', 'TIẾNG TRUNG': '八', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_35', 'TIẾNG VIỆT ': 'Không', 'PHIÊN ÂM': 'bù', 'TIẾNG TRUNG': '不', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': 'Dùng để trả lời câu hỏi '}, {'STT': 'HSK1_1_36', 'TIẾNG VIỆT ': 'Số đếm 6', 'PHIÊN ÂM': 'liù', 'TIẾNG TRUNG': '六', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_37', 'TIẾNG VIỆT ': 'To, lớn', 'PHIÊN ÂM': 'dà', 'TIẾNG TRUNG': '大', 'PHÂN LOẠI': 'Về kích thước', 'Ý NGHĨA': None}, {'STT': 'HSK1_1_38', 'TIẾNG VIỆT ': 'Bầu trời', 'PHIÊN ÂM': 'tiān', 'TIẾNG TRUNG': '天', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_1', 'TIẾNG VIỆT ': 'Cảm ơn', 'PHIÊN ÂM': 'xiè xie', 'TIẾNG TRUNG': '谢谢', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_2', 'TIẾNG VIỆT ': 'Không cần cảm ơn đâu', 'PHIÊN ÂM': 'bú xiè', 'TIẾNG TRUNG': '不谢', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_3', 'TIẾNG VIỆT ': 'Cảm ơn (cô, anh, em,..)', 'PHIÊN ÂM': 'xiè xie nǐ', 'TIẾNG TRUNG': '谢谢你', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_4', 'TIẾNG VIỆT ': 'Đừng khách sáo', 'PHIÊN ÂM': 'bú kè qi', 'TIẾNG TRUNG': '不客气', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_5', 'TIẾNG VIỆT ': 'Tạm biệt', 'PHIÊN ÂM': 'zài jiàn', 'TIẾNG TRUNG': '再见', 'PHÂN LOẠI': 'Giao tiếp cơ bản', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_6', 'TIẾNG VIỆT ': 'Số đếm 3', 'PHIÊN ÂM': 'sān', 'TIẾNG TRUNG': '三', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_7', 'TIẾNG VIỆT ': 'Núi', 'PHIÊN ÂM': 'shān', 'TIẾNG TRUNG': '山', 'PHÂN LOẠI': 'Địa điểm', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_8', 'TIẾNG VIỆT ': 'Đồng hồ', 'PHIÊN ÂM': 'zhōng', 'TIẾNG TRUNG': '钟', 'PHÂN LOẠI': 'Đồ vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_9', 'TIẾNG VIỆT ': 'Con cừu', 'PHIÊN ÂM': 'yáng', 'TIẾNG TRUNG': '羊', 'PHÂN LOẠI': 'Động vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_10', 'TIẾNG VIỆT ': 'Số đếm 0', 'PHIÊN ÂM': 'líng', 'TIẾNG TRUNG': '零', 'PHÂN LOẠI': 'Số đếm', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_11', 'TIẾNG VIỆT ': 'Rau quả', 'PHIÊN ÂM': 'cài', 'TIẾNG TRUNG': '菜', 'PHÂN LOẠI': 'Đồ ăn', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_12', 'TIẾNG VIỆT ': 'Bàn tay', 'PHIÊN ÂM': 'shǒu', 'TIẾNG TRUNG': '手', 'PHÂN LOẠI': 'Bộ phận con người', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_13', 'TIẾNG VIỆT ': 'Con gấu', 'PHIÊN ÂM': 'xióng', 'TIẾNG TRUNG': '熊', 'PHÂN LOẠI': 'Động vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_14', 'TIẾNG VIỆT ': 'Mây', 'PHIÊN ÂM': 'yún', 'TIẾNG TRUNG': '云', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_15', 'TIẾNG VIỆT ': 'Ngôi sao', 'PHIÊN ÂM': 'xīng', 'TIẾNG TRUNG': '星', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_16', 'TIẾNG VIỆT ': 'Nhân dân tệ', 'PHIÊN ÂM': 'yuán', 'TIẾNG TRUNG': '元', 'PHÂN LOẠI': 'Tiền tệ', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_17', 'TIẾNG VIỆT ': 'Mọi người', 'PHIÊN ÂM': 'rén', 'TIẾNG TRUNG': '人', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_18', 'TIẾNG VIỆT ': 'Con thuyền', 'PHIÊN ÂM': 'chuán', 'TIẾNG TRUNG': '船', 'PHÂN LOẠI': 'Phương tiện', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_19', 'TIẾNG VIỆT ': 'Cái giường', 'PHIÊN ÂM': 'chuáng', 'TIẾNG TRUNG': '床', 'PHÂN LOẠI': 'Đồ vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_20', 'TIẾNG VIỆT ': 'Ăn', 'PHIÊN ÂM': 'chī', 'TIẾNG TRUNG': '吃', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_21', 'TIẾNG VIỆT ': 'Nóng', 'PHIÊN ÂM': 'rè', 'TIẾNG TRUNG': '热', 'PHÂN LOẠI': 'Cảm xúc', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_22', 'TIẾNG VIỆT ': 'Tủ lạnh', 'PHIÊN ÂM': 'bīng xīng', 'TIẾNG TRUNG': '冰箱', 'PHÂN LOẠI': 'Đồ vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_23', 'TIẾNG VIỆT ': 'Trứng gà', 'PHIÊN ÂM': 'jī dàn', 'TIẾNG TRUNG': '鸡蛋', 'PHÂN LOẠI': 'Đồ ăn', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_24', 'TIẾNG VIỆT ': 'Tài xế', 'PHIÊN ÂM': 'sī jī', 'TIẾNG TRUNG': '司机', 'PHÂN LOẠI': 'Nghề nghiệp', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_25', 'TIẾNG VIỆT ': 'Bóng đá', 'PHIÊN ÂM': 'zú qiú', 'TIẾNG TRUNG': '足球', 'PHÂN LOẠI': 'Khác', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_26', 'TIẾNG VIỆT ': 'Sân bay', 'PHIÊN ÂM': 'jī chǎng', 'TIẾNG TRUNG': '机场', 'PHÂN LOẠI': 'Địa điểm', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_27', 'TIẾNG VIỆT ': 'Leo núi', 'PHIÊN ÂM': 'pá shǎn', 'TIẾNG TRUNG': '爬山', 'PHÂN LOẠI': 'Hành động', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_28', 'TIẾNG VIỆT ': 'Đồng hồ đeo tay', 'PHIÊN ÂM': 'shǒu biǎo', 'TIẾNG TRUNG': '手表', 'PHÂN LOẠI': 'Đồ vật', 'Ý NGHĨA': None}, {'STT': 'HSK1_2_29', 'TIẾNG VIỆT ': 'Gấu trúc', 'PHIÊN ÂM': 'xióng máo', 'TIẾNG TRUNG': '熊猫', 'PHÂN LOẠI': 'Động vật', 'Ý NGHĨA': None}]

########################################
@api.route('/api', '/api/')
class GetAndPost(Resource):
    def get(self):
        ## GET ALL
        return jsonify(vocabulary.objects.all()) # type: ignore
        ## POST

    
@api.route('/api/<idx>')
class GetUpdateDelete(Resource):
    
    ## GET ONE
    def get(self, idx):
        return jsonify(vocabulary.objects(User_ID = idx))# type: ignore
    
    #PUT
    def put(self, idx):
        data = api.payload
        vocabulary.objects(vocab_ID= idx).update(**data)# type: ignore
        return jsonify(vocabulary.objects(vocab_ID= idx))# type: ignore
    
    #DELETE
    def delete(self,idx):
        vocabulary.objects(vocab_ID= idx) # type: ignore
        return jsonify("User deleted")

##########################################

@app.route("/",methods=['GET', 'POST'])
@app.route("/index")
@app.route("/home",methods=['GET', 'POST'])
def index():
    full_Data = vocabulary.objects( ).all()
    # print(full_Data.phan_Loai)
    if request.method == 'POST':
        selected_word = request.form['Filter_Phan_Loai']
        
        print(selected_word)
        if selected_word == "":
            vocab = vocabulary.objects().all()
        else:
            vocab = vocabulary.objects( phan_Loai = selected_word )
        return render_template("index.html", data = vocab, full_Data = full_Data)
    
    
    vocab = vocabulary.objects().all()
    return render_template("index.html", data=vocab, full_Data = full_Data)

@app.route("/login",methods =['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    
    
    form = LoginForm()
    if form.validate_on_submit():
        username = form.userName.data
        password = form.passWord.data
        
        user_x = user.objects(Username = username).first()# type: ignore
        if user_x and password == user_x.Password:
            flash(f"{user_x.First_Name} finish logging")
            session['User_ID'] =user.User_ID
            session['Username'] =user.Username
            return redirect("/index")
        else:
            flash("Sorry, try again",'danger')
            print(user_x)
    return render_template("login.html", title = "Login", form = form, login = True)

@app.route("/lesson")
def lesson():
    return render_template("lesson.html")

@app.route("/something")
def something():
    return render_template("something.html")

@app.route("/introduction")
def introduction():
    return render_template("introduction.html")

