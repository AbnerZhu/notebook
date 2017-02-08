# 常见问题解决

- 忘记密码

  - version >= 5.6

    ```shell
    mysql -uroot -p 'password' # password 即为 .mysql_secret 里的密码， .mysql_secret 为第一次启动时， root目录下产生的随机密码
    SET PASSWORD = PASSWORD('newpassword')
    ```

  - version < 5.6， 有以下三种方法

    - ```shell
      service mysqld stop
      mysqld_safe --skip-grant-tables &
      mysql -uroot -p # 输入命令回车进入， 出现输入密码提示直接回车
      use mysql;
      update user set password=password('newpassword') where user="root";
      flush privileges;
      quit;
      ```

    - ```shell
      service mysqld stop
      mysqld_safe --skip-grant-tables &
      mysql -uroot -p # 输入命令回车进入， 出现输入密码提示直接回车
      set password for root@localhost = password('newpassword');
      ```

    - ```shell
      /path/mysqladmin -u Username -h Host password 'newpassword' -p
      ```


- 解决bash: mysql:command not found 的方法

  - 这是由于系统默认会查找/usr/bin下的命令，如果这个命令不在这个目录下，当然会找不到命令，我们需要做的就是映射一个链接到/usr/bin目录下，相当于建立一个链接文件。

    :这是由于系统默认会查找/usr/bin下的命令，如果这个命令不在这个目录下，当然会找不到命令，我们需要做的就是映射一个链接到/usr/bin目录下，相当于建立一个链接文件。
    首先得知道mysql命令或mysqladmin命令的完整路径，比如mysql的路径是：/usr/local/mysql/bin/mysql，我们则可以这样执行命令：

    ```shell
    ln -s /usr/local/mysql/bin/mysql /usr/bin
    ```

- mysql 给 root 开启远程访问权限

  - ```shell
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'ysyhl9t' WITH GRANT OPTION;
    ```

    ​