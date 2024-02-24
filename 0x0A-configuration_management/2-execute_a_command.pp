# this manifest carries out a kill command

exec{ 'kill process':
    command => 'pkill killmenow'

}