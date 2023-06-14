import oss2
import os
import argparse

access_key_id = '**'
access_key_secret = '***'

# 填写自己的 Bucket 名称和上传地址
bucket_name = 'hobby-prod'
upload_path = 'release-android/channel_lastest/'

# 创建 OSS 链接
auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, 'https://oss-cn-***.aliyuncs.com', bucket_name)


# 上传文件到 OSS
def oss_upload_file(file_path):
    # 构造上传路径
    file_name = os.path.basename(file_path)
    oss_path = upload_path + file_name
    # 上传文件
    with open(file_path, 'rb') as file_obj:
        result = bucket.put_object(oss_path, file_obj)
    return result.resp.response.url


# 初始化参数构造器
parser = argparse.ArgumentParser()
# 在参数构造器中添加一个命令行参数
parser.add_argument('--file', type=str, default='D:\\hobby\\apk\\hobby_release_gw.apk')
# 获取所有的命令行参数
args = parser.parse_args()

# 测试
# file_path = 'D:\\syz\\test.txt'
file_path = args.file
print('本地图片路径： ' + str(args.file))
oss_url = oss_upload_file(file_path)
# 返回上传地址
print('oss文件存储路径:' + oss_url)
