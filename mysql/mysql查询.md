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

