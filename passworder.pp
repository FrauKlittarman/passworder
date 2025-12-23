#passworder
class passworder (
  $passworder_enabled = true
) {

  package { [ 'pwgen',
    'qrencode',
    'python3-toml', ]:
    ensure => installed,
  }

  file { '/var/local/passworder/':
    ensure  => directory,
    source  => 'puppet:///modules/passworder/',
    recurse => true,
    owner   => root,
    group   => root,
    mode    => '0644',
    purge   => true,
    force   => true,
    ignore  => '__pycache__',
  }

  cron { 'run passworder':
    ensure  => $passworder_enabled ? { true  => 'present', false => 'absent', },
    command => "/usr/bin/python3 /var/local/passworder/main.py",
    user    => root,
    minute  => '*/40'
  }

}
