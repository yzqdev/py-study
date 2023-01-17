param(
    [string]$type
)
if ($type -eq "init")
{
    pipenv run python manage.py migrate
}
else
{
    pipenv run python manage.py runserver
}
