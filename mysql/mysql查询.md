### SQL练习
--  1、查询课程1的成绩 比 课程2的成绩 高 的所有学生的学号；
`SELECT a.sno FROM
(SELECT sno,score FROM sc WHERE cno=1) AS a,
(SELECT sno,score FROM sc WHERE cno=2) AS b
WHERE a.score>b.score AND a.sno=b.sno; `




`
select * from student RIGHT JOIN 
(select a.sno,score1,score2 from (select sc.sno,sc.score as score1  from sc where sc.cno=1) a ,(select sc.sno,sc.score as score2  from sc where sc.cno=2) b where  a.sno=b.sno and  
a.score1>b.score2) c on c.sno=student.sno
`

--  2、查询平均成绩大于60分的同学的学号和平均成绩；
` select sc.sno,avg(score) from sc,student GROUP BY sc.sno  HAVING avg(score)>60
   `
-- 3、查询所有同学的学号、姓名、选课数、总成绩；

`
select student.sno,student.sname,count(sc.cno) ,  sum(sc.score) from sc,student where sc.sno=student.sno GROUP BY sc.sno
`

-- 4、查询姓“李”的老师的个数；
`
select  count(1) from teacher where teacher.tname LIKE '%李%'
`

-- 5、查询没学过“叶平”老师课的同学的学号、姓名；

`
SELECT student.sno,student.sname FROM student
WHERE sno NOT IN (SELECT DISTINCT(sc.sno) FROM sc,course,teacher
WHERE sc.cno=course.cno AND teacher.tno=course.tno AND teacher.tname='叶平');
`
-- 6、查询同时学过课程1和课程2的同学的学号、姓名；

`
SELECT sno, sname FROM student
WHERE sno IN (SELECT sno FROM sc WHERE sc.cno = 1)
AND sno IN (SELECT sno FROM sc WHERE sc.cno = 2);
`
-- 7、查询学过“叶平”老师所教所有课程的所有同学的学号、姓名；
`
select sc.sno,student.sname from sc,student ,course,teacher where  sc.sno=student.sno AND course.cno=sc.cno and teacher.tno=course.tno  and teacher.tname="叶平"
`

`
SELECT a.sno, a.sname FROM student a, sc b
WHERE a.sno = b.sno AND b.cno IN
(SELECT c.cno FROM course c, teacher d WHERE c.tno = d.tno AND d.tname = '叶平');
`
-- 8、查询 课程编号1的成绩 比 课程编号2的成绩 高的所有同学的学号、姓名；
`
SELECT a.sno, a.sname FROM student a,
(SELECT sno, score FROM sc WHERE cno = 1) b,
(SELECT sno, score FROM sc WHERE cno = 2) c
WHERE b.score > c.score AND b.sno = c.sno AND a.sno = b.sno;
`

-- 9、查询所有课程成绩小于60分的同学的学号、姓名

`
SELECT sno, sname FROM student
WHERE sno NOT IN (SELECT DISTINCT sno FROM sc WHERE score > 60);
`
-- 10、查询所有课程成绩大于60分的同学的学号、姓名；
`
select student.sno,student.sname from student where student.sno not in (select DISTINCT(sc.sno) from sc where sc.score<60)
`
-- 11、查询没有学全所有课的同学的学号、姓名；

`
select a.d from (select sc.sno d, count(sc.cno) c from sc GROUP BY sc.sno) a where a.c=(select COUNT(course.cno) from course) 
`

`
select student.sno, student.sname
from student, sc
where student.sno = sc.sno
group by student.sno, student.sname
having count(sc.cno) < (select count(cno) from course);
`


-- 12、查询至少有一门课程 与 学号为1的同学所学课程 相同的同学的学号和姓名；
`
select distinct a.sno, a.sname
from student a, sc b
where a.sno <> 1 and a.sno=b.sno and
b.cno in (select cno from sc where sno = 1);
`

-- 13把“sc”表中“刘老师”所教课的成绩都更改为此课程的平均成绩；



-- 14、查询和2号同学学习的课程完全相同的其他同学学号和姓名；
`
select b.sno, b.sname
from sc a, student b
where b.sno <> 2 and a.sno = b.sno
group by b.sno, b.sname
having sum(cno) = (select sum(cno) from sc where sno = 2);

`
-- 15、删除学习“叶平”老师课的sc表记录；
`
DELETE from  sc_copy where cno in (
select cno from course where tno=(select tno from teacher where tname="叶平"
))
`

--16、向sc表中插入一些记录，这些记录要求符合以下条件：
--将没有课程3成绩同学的该成绩补齐, 其成绩取所有学生的课程2的平均成绩；



-17、按平平均分从高到低显示所有学生的如下统计报表：



--18、查询各科成绩最高分和最低分：以如下形式显示：课程号，最高分，最低分；




-- 19、查询课程号、课程名、各科平均成绩、及格率，按各科平均成绩从低到高和及格率的百分数从高到低顺序；



--20、查询如下课程平均成绩和及格率的百分数(用"1行"显示): 企业管理（001），马克思（002），UML （003），数据库（004）；



--21、查询不同老师所教不同课程平均分, 从高到低显示
`
select teacher.tname,course.cname,avg(sc.score) as 平均分  from sc,teacher,course where course.cno=sc.cno and teacher.tno=course.tno GROUP BY course.cno ORDER BY  平均分 desc;
`


--22、查询如下课程成绩均在第3名到第6名之间的学生的成绩：


--23、统计打印各科成绩,各分数段人数:课程ID,课程名称,[100-85],[85-70],[70-60],[ <60]；



-- 24、查询学生平均分及其名次；

-- 25、查询各科成绩前三名的记录:(不考虑成绩并列情况)；
-- 26、查询每门课程被选修的学生数；
select sc.cno,count(sc.sno) from sc group by sc.cno


<<<<<<< HEAD
------------------------------------------------------------------
--27、查查询出只选修了一门课程的全部学生的学号和姓名；
--思路：联结 + 分组 + HAVING与WHERE的区别
--given answer
`
select sc.sno,count(sc.cno) as count from student, sc where sc.sno=student.sno group by student.sno HAVING count=1
`
-- 28、查询男生、女生人数；

`
select 
(select count(1) from student where ssex = '男') 男生人数,
(select count(1) from student where ssex = '女') 女生人数;
`


--29、查询姓“张”的学生名单；
`

--30、查询同名同性学生名单，并统计同名人数；
=======
-- 27、查查询出只选修了一门课程的全部学生的学号和姓名；
>>>>>>> 8dd4d3a7ce4731a59aa836d1f1956c171236c281
