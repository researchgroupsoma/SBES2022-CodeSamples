select 
'andoid' as framework, 
'googlesamples/android-play-places' as path,
q.Id as question_id,
q.Tags as question_tags,
q.ViewCount as question_view_count,
q.AnswerCount as question_answer_count,
q.Score as question_score,
q.CreationDate as question_creation_date,
'link' as question_link,
q.OwnerUserId as question_owner_id,
u.Reputation as question_owner_reputation,
u.CreationDate as question_owner_creation_date,
'tags' as question_owner_tags,
'preencher' as answer_id,
'preencher' as answer_score,
'preencher' as answer_creation_date,
'preencher' as answer_owner_id,
'preencher' as answer_owner_reputation,
'preencher' as answer_owner_creation_date,
'preencher' as answer_owner_tags,
q.AcceptedAnswerId
from 
Posts as q 
join Users as u on q.OwnerUserId = u.Id
where 
q.CreationDate >= ('05/16/2014') and
q.CreationDate < ('05/16/2016') and
q.PostTypeId = 1 and 
q.Body like('%>https://github.com/googlesamples/android-play-places%')
order by q.Id;







select 
a.Id as answer_id,
a.Score as answer_score,
a.creationDate as answer_creation_date,
a.OwnerUserId as answer_owner_id,
u.Reputation as answer_owner_reputation,
u.CreationDate as answer_owner_creation_date,
'preencher' as answer_owner_tags
from 
Posts as a join Users as u on a.OwnerUserId = u.Id
where
a.Id in 
(
29427054,
29750984,
30382068,
31858505,
51836721
);