-- 1115938
select count(1) from testsmells t;

-- 36138
select count(1) from testsmells t where t.score < 0;

-- 1079800
select count(1) from testsmells t where t.score > 0;

-- 1115938
select count(1) from testsmells t where t.score is not null;

-- Score de negatividade por testsmells
SELECT distinct (testsmell),
    sum(score)
FROM testsmells
where
    score < 0
group by
    testsmell;

-- Score de negatividade por testsmells
SELECT distinct (testsmell),
    sum(score)
FROM testsmells
group by
    testsmell;

SELECT testsmell, AVG(CAST(score AS REAL)) as media_score
FROM testsmells
GROUP BY
    testsmell
ORDER BY media_score ASC;

SELECT testsmell, COUNT(score) as quantidade
FROM testsmells
WHERE
    CAST(score AS REAL) < 0
GROUP BY
    testsmell;

-- soma dos sentimentos negativos
SELECT testsmell, SUM(CAST(score AS REAL)) as total_score
FROM testsmells
WHERE
    CAST(score AS REAL) < 0
GROUP BY
    testsmell
ORDER BY total_score ASC;

-- média dos sentimentos negativos por testsmell
SELECT testsmell, SUM(CAST(score AS REAL)) / COUNT(score) as media
FROM testsmells
WHERE
    CAST(score AS REAL) < 0
GROUP BY
    testsmell
ORDER BY media ASC;

-- soma dos sentimentos negativos por autor
SELECT author, SUM(CAST(score AS REAL)) as total_score
FROM testsmells
WHERE
    CAST(score AS REAL) < 0
GROUP BY
    author
ORDER BY total_score ASC;

-- média dos sentimentos negativos por autor
SELECT author, SUM(CAST(score AS REAL)) / COUNT(score) as media
FROM testsmells
WHERE
    CAST(score AS REAL) < 0
GROUP BY
    author
ORDER BY media ASC;

-- quantidade de projetos por autor
SELECT author, COUNT(DISTINCT project_name) as quantidade
FROM testsmells
GROUP BY
    author
ORDER BY quantidade DESC;

-- projetos por autor
select DISTINCT (ts.project_name)
from testsmells as ts
where
    ts.author like 'Kevin Moore'
limit 100;