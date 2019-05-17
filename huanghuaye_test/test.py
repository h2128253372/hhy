from flask import Blueprint

test_hhy=Blueprint('test_hhy',__name__)

@test_hhy.route('/test_4130',methods=['POST'])
def test_4130():
    return "我"

