# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import redis
host = '192.168.3.229'
passwd = 'Gi3d85028501'
db = 0
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    r = redis.Redis(host=host, port=6379, password=passwd, db=db, decode_responses=True)
    # for k in r.keys('*'):
    #     with open('redis.txt', mode='a+', encoding='utf-8') as f:
    #         f.write('===========================\n'+k+'\n')
    #         f.write(r.get(k)+'\n===========================\n')

    print(r.get('sensitive_words'))