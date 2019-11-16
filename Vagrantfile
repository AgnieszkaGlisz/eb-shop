Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.network "private_network", ip: "10.20.30.40"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbook.yaml"
  end
end
