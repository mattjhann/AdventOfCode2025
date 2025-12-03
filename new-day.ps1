param (
    [string] $day
)

Copy-Item .\template .\day$day -Recurse
New-Item .\day$day\example.txt -ItemType File
New-Item .\day$day\input.txt -ItemType File
New-Item .\day$day\test.txt -ItemType File

(Get-Content .\day$day\__init__.py).Replace('${day}',$day) | Out-File .\day$day\__init__.py -Force -Encoding utf8