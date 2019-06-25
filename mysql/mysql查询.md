### SQL练习
--  1、查询课程1的成绩 比 课程2的成绩 高 的所有学生的学号；
`SELECT a.sno FROM
(SELECT sno,score FROM sc WHERE cno=1) AS a,
(SELECT sno,score FROM sc WHERE cno=2) AS b
WHERE a.score>b.score AND a.sno=b.sno; `

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
