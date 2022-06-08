#!/bin/sh

git filter-branch -f --env-filter '
# 之前的邮箱
OLD_EMAIL="501893067@qq.com"
# 修改后的用户名&密码
CORRECT_NAME="kamalyes"
CORRECT_EMAIL="501893067@qq.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

# git push --force --tags origin 'refs/heads/*'