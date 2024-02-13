import subprocess

print("""\n"""+ "+-++-++-++-++-++-+-+-++-++-++-++-++-++-+\n" + 
        "        K_R_A_T_O_S  F_R_A_M_E_W_O_R_K       \n" +
        "+-++-++-++-++-++-+-+-++-++-++-++-++-++-+\n" +
        "\n" +
        "     CODED BY : P4RADOXE (Rishav Verma)   \n" +
        "           KRATOS FRAMEWORK v.1.          \n" +
        "A Python Based Framework For Ethical Hacking\n\n\n""")

print("1) NMAP Automated Scanning              (Press 1)")
print("2) Finding Exploit                      (Press 2)")
print("3) Full Scanning                        (Press 3)")
print("4) Protocol Scanning (ftp,ssh,smtp etc)  (Press 4)")
print("5) Android Hacking (Any App Injection)  (Press 5)\n\n")

optns = int(input("Select An Option: "))

# (1) NMAP SCANNING SCRIPT#############################################################################
if optns == 1:
    tgt_ip = input("Enter Your Target IP Address: ")
    try:
        # Run the Nmap command
        nmap_output = subprocess.check_output(['nmap', '-Pn', tgt_ip])
        # Print the output
        print(nmap_output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        # Handle error if Nmap command fails
        print("An error occurred while running Nmap:", e)

# (2) SEARCHSPLOIT SCRIPT##############################################################################

elif optns == 2:
    exploit_name = input("Enter the name of the exploit to search: ")
    try:
        # Run the searchsploit command
        searchsploit_output = subprocess.check_output(['searchsploit', exploit_name])
        # Print the output
        print(searchsploit_output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        # Handle error if searchsploit command fails
        print("An error occurred while searching for exploit:", e)


# (3) FULL SCANNING SCRIPT##############################################################################

elif optns == 3:
    ipadr = input("Enter Domain Or IP Address: ")
    try:
        scan_output = subprocess.check_output(['nmap', '-A', '-v', ipadr])
        print(scan_output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("An Error Occured While Doing Full Scanning")


# (4) PROTOCOL SCANNING SCRIPT##########################################################################

elif optns == 4:
    vict_ip = input("Enter Domain Or Ip Address: ")
    try:
        scan_output = subprocess.check_output(['nmap', '-sO', '-v', vict_ip])
        print(scan_output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("An Error Occur During The Protocol Scanning:", e)


# (5) ANDROID HACKING SCRIPT######################################################################

elif optns == 5:
    bash_script_path = "./bin.sh"
    try:
      subprocess.run(["bash", bash_script_path], check=True)
    except subprocess.CalledProcessError as e:
     print("Error occurred while executing the Bash script:", e)