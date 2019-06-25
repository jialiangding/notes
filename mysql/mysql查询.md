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
