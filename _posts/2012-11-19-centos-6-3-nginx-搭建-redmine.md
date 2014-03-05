---
layout: default
title: CentOS 6.3 Nginx 搭建 Redmine
---
安装 Redmine 2.0.3
创建一个安装目录

 	cd /var/www/
下载 redmine

	 wget http://rubyforge.org/frs/download.php/76259/redmine-2.0.3.tar.gz
解压

	tar -zxvf redmine-2.0.3.tar.gz
重命名

	 mv /var/www/redmine-2.0.3 /var/www/redmine
删除安装包

	rm redmine-2.0.3.tar.gz
回到根目录

	 cd /
安装需要使用的库

	yum -y install zlib-devel curl-devel openssl-devel apr-devel apr-util-devel mysql-devel
安装 Ruby
对于 redmine 2.0.3 我们使用 ruby 1.9.3

	 wget http://ftp.ruby-lang.org/pub/ruby/stable/ruby-1.9.3-p0.tar.gz
解压

	 tar -zxvf ruby-1.9.3-p0.tar.gz
	 cd ruby-1.9.3-p0/
编译安装

	./configure
	make
	make install
查看版本号

	ruby -v
你将会看到

	ruby 1.9.3p0 (2011-10-30 revision 33570) [x86_64-linux]

如果运行顺利的话 “RubyGems Install“.
 
如果出现了问题  ruby -v 不工作

	# which ruby # TO CHECK WHERE IT SHOULD BE
	# whereis ruby # TO CHECK WHERE IT IS INSTALLED
	which returns like /usr/bin/ along with other directories (where ruby is expected to be), and whereis returns like /usr/local/bin/ruby (thats where ruby actually lies).
	Fix via adding /usr/local/bin to $PATH
	# vi /etc/profile

添加到文件里面去

	#Path manupulation
	if["$EUID"="0"];then
	pathmunge /sbin
	pathmunge /usr/sbin
	pathmunge /usr/local/sbin
	pathmunge /usr/local/bin # ADDED THIS
	else
	pathmunge /usr/local/bin after # ADDED THIS
	pathmunge /usr/local/sbin after
	pathmunge /usr/sbin after
	pathmunge /sbin
	fi
或者在文件地步添加

	# nano /etc/profile
	export PATH="$PATH:/usr/local/bin"
前面的是为root之外的用户，为root添加

	# nano ~/.bashrc
	export PATH="$PATH:/usr/local/bin"

重新登录账户以完成更改
	
	Fix via Symlink Creation
	This is not recommended, since if the ruby dependency is broken, others will likely be later on, too. Repair this by adding the folder to the $PATH variable like described before, else gem, rake, bundle, passenger-install-apache2-module will not work either… you would have to create symlinks for them later on, too.
	Symlinks are created like this
 
链接一下子

	# ln -s /usr/local/bin/ruby /usr/bin/ruby   
在看看ruby是否工作 

	# which ruby # MUST RETURN PATH TO RUBY
	# ruby -v # MUST RETURN RUBY VERSION
	cd ..
	Now it has to work. When changing $PATH variable, did you log out and log on again with your current user?
	If this does not function properly, other things later on will also not work.
安装 RubyGems 1.8

	# cd
	# wget http://rubyforge.org/frs/download.php/74806/rubygems-1.8.0.tgz
解压

	# tar zxvf rubygems-1.8.0.tgz
安装

	# cd rubygems-1.8.0
	# ruby setup.rb
查看gem是否好使

	#gem -v
如果少了YAML的话…. 

	#wget http://pyyaml.org/download/libyaml/yaml-0.1.4.tar.gz
	# ./configure
	# make
	# make install
安装 Phusion Passenger

	# cd /usr/local/lib/ruby/gems/1.9.1/gems/
	# wget http://rubyforge.org/frs/download.php/76005/passenger-3.0.12.tar.gz
	# tar zxvf passenger-3.0.12.tar.gz
	# cd passenger-3.0.12
	# ./bin/passenger-install-nginx-module
选择1 继续前进 如果少什么库就安一下

	# nano passenger.conf
	# cd /etc/nginx/conf.d
 
在nginx的配置文件里添加如下内容：（详情请见nginx.conf）

	passenger_root /usr/local/lib/ruby/gems/1.9.1/gems/passenger-3.0.12;
	passenger_ruby /usr/local/bin/ruby;
在server里添加如下内容：（详情请见nginx.conf）

	passenger_enabled on;
	passenger_use_global_queue on;
重启 Nginx

	 /etc/init.d/nginx restart
Redmine Setup
	# cd /var/www/redmine/

首先安装 bundler

	# gem install bundler
然后安装gems 

	# bundle install --without development test
我们的用的是mysql 然后把postresql  和 sqlite 都忽略了吧~

	bundle install --without development test postgresql sqlite rmagick
如果你没有安装 ImageMagick, 你可以忽略rmagick: ‘bundle install –without development test rmagick’.

如果要安装  ImageMagick 的话。。。

	yum install ImageMagick
	yum install ImageMagick-devel
 
这里还有以一个问题 貌似是没有添加mysql 

	vi /var/www/redmine/Gemfile
在文件适当的位置添加

	gem "mysql" 
创建一个数据库

	For MySQL:
	create database redmine character set utf8;
	create user 'redmine'@'localhost' identified by'my_password';
	grant all privileges on redmine.* to 'redmine'@'localhost';
 
Mysql 5.02 之前的版本 最后一句改成这样子

	grant all privileges on redmine.* to 'redmine'@'localhost' identified by'my_password';

For PostgreSQL:

	CREATE ROLE redmine LOGIN ENCRYPTED PASSWORD 'my_password' NOINHERIT VALID UNTIL 'infinity';
	CREATE DATABASE redmine WITH ENCODING='UTF8' OWNER=redmine;
　　
 
数据库环境配置

	# cd config
	# mv database.yml.example database.yml
	# vi database.yml
数据库文件设置：

	production:
	adapter: mysql
	database: redmine
	host: localhost
	username: redmine
	password: my_password
　　
如果出现port (3306), 就像下面这样:
	
	production:
	adapter: mysql
	database: redmine
	host: localhost
	port:3307
	username: redmine
	password: my_password
	　　
	Example for a PostgreSQL database (default port):
	production:
	adapter: postgresql
	database:<your_database_name>
	host:<postgres_host>
	username:<postgres_user>
	password:<postgres_user_password>
	encoding: utf8
	schema_search_path:<database_schema>(default-public)
	　　
Generate a session store secret.

	# cd /var/www/redmine/
	# rake generate_secret_token

创建数据库基本信息 表…
	# RAILS_ENV=production rake db:migrate
	It will create tables and an administrator account.
如果出现以下错误
	
	Rake aborted!
	no such file to load — net/https
说明你又少了什么库 然后就再去安装一下吧
 
	you need to install libopenssl-ruby1.8, in Ubuntu, just like this: apt-get install libopenssl-ruby1.8

创建默认数据内容：

	# RAILS_ENV=production rake redmine:load_default_data
nginx.conf文件的内容：
	 
	http {
	    include       mime.types;
	    default_type  application/octet-stream;
	 
	    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
	    #                  '$status $body_bytes_sent "$http_referer" '
	    #                  '"$http_user_agent" "$http_x_forwarded_for"';
	 
	    #access_log  logs/access.log  main;
	 
	    passenger_root /usr/local/lib/ruby/gems/1.9.1/gems/passenger-3.0.12;
	    passenger_ruby /usr/local/bin/ruby;
	 
	    sendfile        on;
	    #tcp_nopush     on;
	 
	    #keepalive_timeout  0;
	    keepalive_timeout  65;
	 
	    #gzip  on;
	    server {
	                listen 80;
	 
	 
	                server_name nenu.pandawork.net;
	 
	                root   /var/www/redmine/public;
	 
	                index index.html index.htm;
	 
	                passenger_enabled on;
	                passenger_use_global_queue on;
	 
	                error_page 400 /error/400.html;
	                error_page 401 /error/401.html;
	                error_page 403 /error/403.html;
	                error_page 404 /error/404.html;
	                error_page 405 /error/405.html;
	                error_page 500 /error/500.html;
	                error_page 502 /error/502.html;
	                error_page 503 /error/503.html;
	 
	                error_log /var/www/redmine/log/production.log;#这个我也不确定 然后就这么写了 日志文件 不影响运行就是了
	               #access_log /var/log/projects.domain.net/access.log combined;
	 
	 
	                ## Set the OS file cache.
	                open_file_cache max=3000 inactive=120s;
	                open_file_cache_valid 45s;
	                open_file_cache_min_uses 2;
	                open_file_cache_errors off;
	 
	        ## Support for favicon. Return an 1x1 transparent GIF if it doesn't
	        ## exist.
	        location = /favicon.ico {
	                expires 30d;
	                try_files /favicon.ico @empty;
	        }
	 
	                # serve static files directly
	                location ~* ^.+.(jpg|jpeg|gif|css|png|js|ico|html|xml|txt)$ {
	                           access_log           off;
	                }
	 
	}
	}
	　　
 
参考文章：http://www.devcu.com/forums/topic/311-install-redmine-203-nginx-centos-6/#entry1373