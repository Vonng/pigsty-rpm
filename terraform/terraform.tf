# add your credentials here or pass them via env
# export ALICLOUD_ACCESS_KEY="????????????????????"
# export ALICLOUD_SECRET_KEY="????????????????????"
# e.g : ./aliyun-key.sh
provider "alicloud" {
  # access_key = "????????????????????"
  # secret_key = "????????????????????"
}

# use 10.10.10.0/24 cidr block as demo network
resource "alicloud_vpc" "vpc" {
  vpc_name   = "pigsty-demo-network"
  cidr_block = "10.10.10.0/24"
}

# add virtual switch for pigsty demo network
resource "alicloud_vswitch" "vsw" {
  vpc_id     = "${alicloud_vpc.vpc.id}"
  cidr_block = "10.10.10.0/24"
  zone_id    = "cn-beijing-i"
}

# add default security group and allow all tcp traffic
resource "alicloud_security_group" "default" {
  name   = "default"
  vpc_id = "${alicloud_vpc.vpc.id}"
}
resource "alicloud_security_group_rule" "allow_all_tcp" {
  ip_protocol       = "tcp"
  type              = "ingress"
  nic_type          = "intranet"
  policy            = "accept"
  port_range        = "1/65535"
  priority          = 1
  security_group_id = "${alicloud_security_group.default.id}"
  cidr_ip           = "0.0.0.0/0"
}

# pg-meta: 1c2G x1
# pg-test: 1c1G x3

# Available IMAGES
# CentOS 7.9   :  centos_7_9_x64_20G_alibase_20230815.vhd
# Rocky 8.8    :  rockylinux_8_8_x64_20G_alibase_20230613.vhd
# Rocky 9.2    :  rockylinux_9_2_x64_20G_alibase_20230613.vhd
# Ubuntu 20.04 :  ubuntu_20_04_x64_20G_alibase_20230815.vhd
# Ubuntu 22.04 :  ubuntu_22_04_x64_20G_alibase_20230815.vhd
# Anolis 8.8   :  anolisos_8_8_x64_20G_rhck_alibase_20230804.vhd
# Debian 11.7  :  debian_11_7_x64_20G_alibase_20230718.vhd

# https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/instance
resource "alicloud_instance" "el8" {
  instance_name              = "el8"
  host_name                  = "el8"
  instance_type              = "ecs.s6-c1m2.small"
  vswitch_id                 = "${alicloud_vswitch.vsw.id}"
  security_groups            = ["${alicloud_security_group.default.id}"]
  image_id                   = "rockylinux_8_8_x64_20G_alibase_20230613.vhd"
  password                   = "PigstyDemo4"
  private_ip                 = "10.10.10.10"
  internet_max_bandwidth_out = 40 # 40Mbps , alloc a public IP
}

resource "alicloud_instance" "el9" {
  instance_name              = "el9"
  host_name                  = "el9"
  instance_type              = "ecs.s6-c1m2.small"
  vswitch_id                 = "${alicloud_vswitch.vsw.id}"
  security_groups            = ["${alicloud_security_group.default.id}"]
  image_id                   = "rockylinux_9_2_x64_20G_alibase_20230613.vhd"
  password                   = "PigstyDemo4"
  private_ip                 = "10.10.10.11"
  internet_max_bandwidth_out = 40 # 40Mbps , alloc a public IP
}


output "el8_ip" {
  value = "${alicloud_instance.el8.public_ip}"
}

output "el9_ip" {
  value = "${alicloud_instance.el9.public_ip}"
}