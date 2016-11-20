import random
import datetime

def create_message_from_wechat(
    to_user='to_user',
    from_user='from_user',
    create_time=datetime.datetime.now().timestamp(),
    msg_type='text',
    content='content',
    msg_id=None):
    if not msg_id:
        msg_id=random.randint(0, (2 << 64) - 1)

    return '''<xml>
 <ToUserName><![CDATA[{}]]></ToUserName>
 <FromUserName><![CDATA[{}]]></FromUserName>
 <CreateTime>{}</CreateTime>
 <MsgType><![CDATA[{}]]></MsgType>
 <Content><![CDATA[{}]]></Content>
 <MsgId>{}</MsgId>
 </xml>'''.format(to_user, from_user, create_time, msg_type, content, msg_id)
