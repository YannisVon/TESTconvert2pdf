import requests
import os
import threading
from time import ctime

test_url = "http://172.20.100.220:8888/PDFService/api/PDF/convert2pdf"

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    print("Start time : %s" %(ctime()))
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath,"/"+ allDir))
        convert2pdf(child,allDir)



def convert2pdf(pathName,name):
        files = {'file': open(pathName, 'rb')}
        try:
            result = requests.post(test_url,files=files)
            result.raise_for_status()
            content = result.content
            if content==(b''):
                print(name)
            else:
                #name = name.split('.')[0]
                (name,ext) = name.split('.')
                with open('f:/result/' + name + '.pdf', 'wb') as fp:
                    fp.write(content)
            print('return value: %r' % (content))
        except requests.RequestException as e:
            print(e)
        else:
            print('did it')

filePathOne = 'F:/周二课堂'
filePathTwo = 'F:/有问题'
threads = []
threadOne = threading.Thread(target=eachFile, args=(filePathOne,))
threads.append(threadOne)
threadTwo = threading.Thread(target=eachFile, args=(filePathTwo,))
threads.append(threadTwo)

# 断言接口返回值
# assert resultJsonFormat['status']==200


if __name__ == '__main__':
    #filepath = 'F:/convert2pdf/convert2pdf/file2convert'
    #eachFile(filePath)
    for t in threads:
        #setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
        t.setDaemon(True)
        t.start()
    #join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
    t.join()