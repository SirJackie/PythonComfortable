@echo off

pip install cefpython3 -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple
pip install pywin32 -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple
pip install easygui -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple

echo 已完成开发环境配置，按任意键退出程序。
pause>nul
