# this manifest installs flask version 2.1

package{ 'flask':
    ensure   => '2.1.0',
    provider => 'pip3'

}