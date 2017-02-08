##### MyBatis 自增主键配置
<link rel="stylesheet" href="http://yandex.st/highlightjs/6.1/styles/default.min.css">
<script src="http://yandex.st/highlightjs/6.1/highlight.min.js"></script>
<script>
hljs.tabReplace = ' ';
hljs.initHighlightingOnLoad();
</script>

- 不返回自增主键值
- 插入后获取自增主键值
- 小结

###### 不返回自增主键值
如果考虑到插入数据的主键不作为其他表插入数据的外键使用， 那么可以考虑使用这种方式。   
1. Oracle Sequence 配置

    <sql id='TABLE_NAME'>TEST_USER</sql>
    <sql id='TABLE_SEQUENCE'>SEQ_TEST_USER_ID.nextval</sql>
    <!-- 注意这里直接调用sequence的nextval函数 -->
    <insert id="insert" parameterType="User">
        insert into <include refid="TABLE_NAME" /> (ID,NAME,AGE)
        values ( <include refid="TABLE_SEQUENCE" /> ,#{name}, #{age} )
    </insert>
    