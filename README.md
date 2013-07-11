//==========================================================================
    JuJu_Backend按业务逻辑以包的形式来组织目录结构，例如与user相关的业务逻辑在
    users包下，与action相关的逻辑处理在actions包下，所有的接口封装在api包下，并
    以Flask蓝图的形式将相关的接口组织起来，在api包声明的蓝图会自动在app注册。
    根目录下的几个文件作用如下：
        app.py:应用程序入口
        helpers.py:应用程序的helper类
        models.py:将所有的model组织在一起
        services.py:将所有service组织在一起
        settings.py:配置文件
        requirements.txt:应用程序依赖
//==========================================================================
