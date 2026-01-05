# Getting Started with Authentication via Key-Pairs

This documentation assumes you have **NEVER** done anything with keypairs before (or at least that you have no recollection of having done so). If you have done keypair stuff for CS 261, you can likely [skip to the github section below](#tell-github-to-join-the-party).
Most of the sections of this document assume you have first followed the preceding sections (so you should strongly consider following them in order).

## Prerequisites

1.  If it isn't already installed on your computer, [install git](https://git-scm.com/downloads/).
    - To tell if it's installed,
        1.  Linux or macOS:
            1.  use the built-in search feature of your operating system to search for "terminal" and launch it.
            2.  type `git --version` and press Enter. Keep this terminal around for all the future steps!
        2.  Windows:
            1.  Press the windows key on the keyboard and search for "bash". If git bash is found and installed, launch it.
            2.  type `git --version` and press Enter. Keep this terminal around for all the future steps!

## Generating a Key Pair

1.  Open a terminal window (specifically as specified above in the prerequisites).
2.  In the terminal Type `ssh-keygen -t ed25519 -b 4096 -C "Generated $(date -I)"`
    1.  when prompted for where to save the key, press Enter to save it in the default location.
    2.  when prompted for a passphrase, do not enter one, just press enter to leave it blank.
        - the whole reason we're setting this keypair authentication up is to avoid having to enter a password every time we perform actions that communicate with a server, which in some cases may be quite frequently.
    3.  leave it blank (just press enter) a second time to confirm you meant it.
    4.  you will see a message like
    ```
    Your identification has been saved in ~/.ssh/id_ed25519
    Your public key has been saved in ~/.ssh/id_ed25519.pub
    The key fingerprint is:
    SHA256:dkzGbszeCq4x+N6nDzqwertya0si5CWQ4MQCHMW7Ju0 Generated 2024-10-07
    The key's randomart image is:
    +---[ed25519 4096]----+
    |*o+.             |
    |=+ .     .       |
    |+.  .     +      |
    |.  ....  B       |
    | o... . S B      |
    |o.o+ + o = .     |
    |..= + = o + .    |
    | . Eo+.= +.o     |
    |   .o*=.++o      |
    +----[SHA256]-----+
    ```

## Configure your computer's ssh client

Tell your computer you'd like to use this key to connect to JMU CS's student server, "stu".

1.  Edit your ssh config (located at `~/.ssh/config`) to include the following lines:
    - If you're not sure how to edit your ssh config, try entering the following in your terminal (see prerequisite above for help opening the correct terminal for our purposes on your OS): `code ~/.ssh`
    - If you don't have a file named config in this location create one
    ```
    Host *
      ServerAliveInterval 30
      ServerAliveCountMax 120
      AddKeysToAgent yes # https://man.openbsd.org/ssh_config#AddKeysToAgent
      # IdentitiesOnly yes # I am thinking maybe I should not propose this for beginners. so it's commented out now.

    Host stu  # by specifying the host here as "stu", you can use "stu" as a shorthand for
              # the full hostname when connecting via ssh to the server at the HostName below
      HostName stu.cs.jmu.edu
              # next setting only necessary if you aren't using a default-named key like id_rsa or id_ed25519
              # IdentityFile ~/.ssh/name-of_non_default_private_key
      User YOUR_EID_BUT_DONT_CAPITALIZE_IT # if you specify a user, you don't have to put the
              # user@ when connecting via ssh
    ```

**NOTICE THE PART YOU HAVE TO REPLACE ABOVE, FOR MOST IT'S IN JUST THE LAST LINE WHERE IT SAYS "YOUR_EID"**

## Tell stu this is all legit

1.  in your terminal (see [prerequisite above for help opening the correct terminal for our purposes on your OS](#prerequisites)), enter `ssh-copy-id stu`
    1.  you may see a message like `%%The authenticity of host 'stu.cs.jmu.edu (134.126.141.221)' can't be established. ED25519 key fingerprint is SHA256:RYxaUOHGdifpo+JaJeE6JHWVqiji+in1GI5lvbJluPk. This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?%%`, if you do, enter "yes"
    2.  you will be prompted for your (JMU EID) password. Enter it. **NOTE: As you type your password, it is possible that nothing will be displayed in the terminal to protect your security.**
    3.  you should see a message like `Number of key(s) added: 1`
    4.  you should now be able to ssh to stu without entering a password. try it: `ssh stu`
        - logout before proceeding to the next step by entering `logout`

## Tell Github to join the party

**Note: For those who skipped here because of 261 reasons - Open a terminal window (specifically as specified [above in the prerequisites](#prerequisites)).**

If you want to do things with GitHub, you must first have an account. If you don't have one yet, [sign up for a GitHub account](https://github.com/signup).

**Note:** it's possible that your quippy username that's served you well since middle school through that very public social media posting about that awkward thing that happened back in high school might be ok to keep around, but perhaps not as your personal-professional username. So maybe don't [doxx](https://en.wikipedia.org/wiki/Doxing) yourself by making your github username relate to all your prior online activity. 😅

1.  Go to [Your GitHub SSH and GPG keys settings \> New SSH Key page](https://github.com/settings/ssh/new).
    - authenticate with GitHub if necessary.
2.  Enter a name for the SSH key.
    - I suggest naming it based on the current computer you are using (try to be imaginative here. Imagine that this is but the first of many of ThatBrand™️ LapFlaps®️ that you will own in your long, laudable career). Consider something like, `ThatDellWithThatOSv42`.
3.  leave the browser there for a sec, and go back to your terminal and show your PUBLIC key to yourself by entering `cat ~/.ssh/id_ed25519.pub`
    - copy ALL of the output (not just the key string of numbers and letters) of that command.
4.  go back to the browser and paste your PUBLIC key's contents into the "Key" field.
5.  click "Add SSH key".
6.  test that all is well by entering `ssh -T git@github.com`
    - you may get a message like this when first connecting to GitHub (It's okay to say yes to this):
    ```
    The authenticity of host 'github.com (140.82.114.4)' can't be established.
    ED25519 key fingerprint is SHA256:+DiY3wvvxxxfxfffF/zLDA0zPMSvHdkr4UvCOqU.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```
    - you should see a message like ''%%Hi hcientist! You've successfully authenticated, but GitHub does not provide shell access.%%''
