# Unit 6 Homework Assignment: PCAPs for Days

In this homework assignment, you will be using the concepts you've learned in class to do some investigative forensics with PCAP files. In addition, you'll capture some of your own home network traffic and parse the results.

There are a few concepts we haven't covered here! You'll have to do some research to fill in gaps in your knowledge.

### Before You Begin

1. From within your Google Drive, create a folder called **05-Wireshark-Analysis**.

2. Right-click the **05-Wireshark-Analysis** folder and select **Get Shareable Link**. You will use this folder to submit your homework when complete and the folder needs to be shareable so we can access it.

3. Inside your **05-Wireshark-Analysis** folder, include three subfolders (Challenge-1, Challenge-2, Challenge-3), one for each of the assignments.

## Challenge 1: Dissecting Mystery PCAPs

You as a network admin have just been told that 3 different protocols are being used on your network, and have been asked to investigate.

- Open up [Resources/Chal-1_Mystery-PCAPs](Resources/Chal-1_Mystery-PCAPs)

  - In this folder, you'll find three "mystery.pcapng" files.

- To complete this challenge, you'll submit 3 documents in your **Challenge-1** folder, one for each mystery file. Name the files `1-Mystery`, `2-Mystery`, and `3-Mystery`.

- In each document, you should include:

  1. A title indicating what application-layer protocol is being used.

  2. 1-2 paragraphs explaining how that protocol works and what it is used for. Include images and diagrams as necessary. Explain the steps taken in communication of the protocol.

     - Include an image of the back-and-forth communication the protocol did in the pcap to help illustrate your explanation.

  3. 2-3 paragraphs explaining what happened in the communication across the network.

     - You should at least answer:

       - Who was sending/receiving information?

       - What was the topic of conversation?

       - What data was transmitted?

     - Include information such as ports used, source/destination IPs, and how much data was transmitted.

     - **Use images throughout to explain how you found this information.**

  4. Any other information of note related to the PCAP file.

## Challenge 2: Homework Network Analysis

After looking at bad traffic at work all day, you start to wonder what's going on on your home network.

- Run a capture on your homework network on any device. Leave the capture running in the background for 2+ hours. Be sure to use the device some while it is running!

- Stop the capture.

- Identify at least 2 instances of suspicious, interesting, and/or unfamiliar protocols/communication.

- To complete this challenge, you'll submit a document named `Home-Analysis` in your **Challenge-2** folder. It should include:

  - A 2-3 paragraph write-up for each of the communication examples (4-6 paragraphs total).

  - Images and screenshots to communicate how you found the communication, and how you investigated it.

  - An explanation of any unfamiliar protocols and how they work, if relevant.

  - A description of the purpose and outcome of that communication.

## Challenge 3: (Bonus) File Carving

Wireshark also allows you to extract files from protocols. This can be really interesting and helpful in reconstructing things like images!

Using your wits and the internet, determine how to extract **files** with different protocols using Wireshark. (Recommended reading: <https://www.sans.org/reading-room/whitepapers/tools/extracting-files-network-packet-captures-36562> section 4.6 - Wireshark)

- Open up [Resources/Chal-3_File-Carving](Resources/Chal-3_File-Carving). In this folder you'll find 3 packet capture files.

- Submit three documents in the **Challenge-3** folder, one for each file. Name the files 1-Carving, 2-Carving, and 3-Carving.

- In each file:

  - Explain the approach you took in finding the file (with images/screenshots) and a description of what you found.

  - Answer the following questions and show the following steps.

### Carving 1:

- Open [ftp_image.pcapng](Resources/Chal-3_File-Carving/ftp_image.pcapng).

- Reconstruct the image the user downloaded.

  - Where were they?

  - When did they last edit the file?

  - What operating system did they use? What was the date?

### Carving 2

- Open [ftp_transfer.pcapng](Resources/Chal-3_File-Carving/ftp_image.pcapng).

- What's the user's username? What's their password?

- Reconstruct the user's spreadsheet.

  - What does it look like they were collecting data on?

### Carving 3

- Open [http_page.pcapng](Resources/Chal-3_File-Carving/http_page.pcapng).

- What's the name of the article the user was reading?

- Find the name of the HTML file/webpage the user was reading. Download it.

- Open the file in a text editor. Do a `Ctrl+F` search for `<img`.

  - This is the start of an "image" tag in HTML.

  - You should find 11 filenames ending in `jpg`. Write these down in a list.

- See how many of these images you can find and download in Wireshark.

  - You won't be able to find all of them. Look carefully at the links for each image. Why can you find some and not others?

- Bonus: Use `curl` to download one of the files you can't find in Wireshark.

-----

## Copyright

Trilogy Education Services © 2018. All Rights Reserved.
