resource "aws_instance" "franklin-iac" {
  connection {
    user        = "centos"
    timeout     = "1m"
    #agent       = false
    private_key = "${file("/home/thedevilsvoice/.ssh/do_terra_rsa")}"
  }
  #ami           = "ami-d2c924b2"
  #ami           = " ami-0776d02f10dd9661f"
  ami           = "${var.amis}"
  instance_type = "t2.micro"
  key_name      = "${var.key_name}"
  # comma separated list of groups
  vpc_security_group_ids = ["${aws_security_group.newb_sec_grp.id}"]
  subnet_id = "${aws_subnet.newb_actual.id}"
  associate_public_ip_address = true
  tags {
    Name = "newb_actual"
  }

  provisioner "file" {
    source      = "conf/setup.sh"
    destination = "/home/admin/setup.sh"
  }

  provisioner "file" {
    source      = "../../credentials.py"
    destination = "/home/admin/credentials.py"
  }

  #provisioner "file" {
  #  source      = "conf/bot.py"
  #  destination = "/home/admin/bot.py"
  #}

  provisioner "remote-exec" {
    inline = [
      "export PATH=$PATH:/usr/bin",
      "sudo apt-get updatei && sudo apt-get upgrade -y",
      "sudo bash /home/admin/setup.sh",
    ]
  }

}
