-- До использования prefetch_related
SELECT "blogapp_article"."id",
       "blogapp_article"."title",
       "blogapp_article"."content",
       "blogapp_article"."pub_date",
       "blogapp_article"."author_id",
       "blogapp_article"."category_id"
FROM "blogapp_article";
args=();
alias=default
SELECT "blogapp_author"."id", "blogapp_author"."name", "blogapp_author"."bio"
FROM "blogapp_author"
WHERE "blogapp_author"."id" = 1
LIMIT 21;
args=(1,);
alias=default
SELECT "blogapp_category"."id", "blogapp_category"."name"
FROM "blogapp_category"
WHERE "blogapp_category"."id" = 3
LIMIT 21;
args=(3,);
alias=default
SELECT "blogapp_tag"."id", "blogapp_tag"."name"
FROM "blogapp_tag"
         INNER JOIN "blogapp_article_tags" ON ("blogapp_tag"."id" = "blogapp_article_tags"."tag_id")
WHERE "blogapp_article_tags"."article_id" = 1;
args=(1,);
alias=default
SELECT "blogapp_author"."id", "blogapp_author"."name", "blogapp_author"."bio"
FROM "blogapp_author"
WHERE "blogapp_author"."id" = 2
LIMIT 21;
args=(2,);
alias=default
SELECT "blogapp_category"."id", "blogapp_category"."name"
FROM "blogapp_category"
WHERE "blogapp_category"."id" = 5
LIMIT 21;
args=(5,);
alias=default
SELECT "blogapp_tag"."id", "blogapp_tag"."name"
FROM "blogapp_tag"
         INNER JOIN "blogapp_article_tags" ON ("blogapp_tag"."id" = "blogapp_article_tags"."tag_id")
WHERE "blogapp_article_tags"."article_id" = 2;
args=(2,);
alias=default
SELECT "blogapp_author"."id", "blogapp_author"."name", "blogapp_author"."bio"
FROM "blogapp_author"
WHERE "blogapp_author"."id" = 4
LIMIT 21;
args=(4,);
alias=default
SELECT "blogapp_category"."id", "blogapp_category"."name"
FROM "blogapp_category"
WHERE "blogapp_category"."id" = 1
LIMIT 21;
args=(1,);
alias=default
SELECT "blogapp_tag"."id", "blogapp_tag"."name"
FROM "blogapp_tag"
         INNER JOIN "blogapp_article_tags" ON ("blogapp_tag"."id" = "blogapp_article_tags"."tag_id")
WHERE "blogapp_article_tags"."article_id" = 3;
args=(3,);
alias=default
SELECT "blogapp_author"."id", "blogapp_author"."name", "blogapp_author"."bio"
FROM "blogapp_author"
WHERE "blogapp_author"."id" = 3
LIMIT 21;
args=(3,);
alias=default
SELECT "blogapp_category"."id", "blogapp_category"."name"
FROM "blogapp_category"
WHERE "blogapp_category"."id" = 3
LIMIT 21;
args=(3,);
alias=default
SELECT "blogapp_tag"."id", "blogapp_tag"."name"
FROM "blogapp_tag"
         INNER JOIN "blogapp_article_tags" ON ("blogapp_tag"."id" = "blogapp_article_tags"."tag_id")
WHERE "blogapp_article_tags"."article_id" = 4;
args=(4,);
alias=default




-- После оптимизации
SELECT "blogapp_article"."id",
       "blogapp_article"."title",
       "blogapp_article"."pub_date",
       "blogapp_article"."author_id",
       "blogapp_article"."category_id",
       "blogapp_author"."id",
       "blogapp_author"."name"
FROM "blogapp_article"
         INNER JOIN "blogapp_author" ON ("blogapp_article"."author_id" = "blogapp_author"."id");
args=();
alias=default
SELECT ("blogapp_article_tags"."article_id") AS "_prefetch_related_val_article_id",
       "blogapp_tag"."id",
       "blogapp_tag"."name"
FROM "blogapp_tag"
         INNER JOIN "blogapp_article_tags" ON ("blogapp_tag"."id" = "blogapp_article_tags"."tag_id")
WHERE "blogapp_article_tags"."article_id" IN (1, 2, 3, 4);
args=(1, 2, 3, 4);
alias=default
SELECT "blogapp_category"."id", "blogapp_category"."name"
FROM "blogapp_category"
WHERE "blogapp_category"."id" IN (1, 3, 5);
args=(1, 3, 5);
alias=default