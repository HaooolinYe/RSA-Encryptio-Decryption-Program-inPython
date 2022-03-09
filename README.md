<h1 id="opener"> RSA-Encryptio-Decryption-Program-inPython <img src="https://user-images.githubusercontent.com/90864900/157359880-1c55654d-7b1f-45e5-9494-e9035d6d09ba.png" width=50 height=50></h1>
A <em>Python program</em> that is able to do <em>RSA encryption</em> and <em>decryption</em>. A valid message to be encrypted or an output decrypted meessage could contain any of the <strong>26 English alphabets</strong> and the <strong>common puncutation marks</strong>.

<p align="center">
<img src="https://user-images.githubusercontent.com/90864900/157359529-76ad4562-befc-4b65-9f72-43342c320bd6.png" height=400 width=700>
</p>

<h2 id="gd"> Guide </h2>
<ul>
  <li><strong><a href="#py">Python Installation</a></strong></li>
  <li><a href="#menu">
    <strong>Menu</strong></a>
    <ol>
      <li>Encryption</li>
      <li>Decryption</li>
    </ol>
  </li>
  <li><strong>Handy Maths Concepts</strong>
      <ol>
      <li>Self-made ASCCI table</li>
      <li>Find Prime through √</li>
      <li>Euclidean Algorithm</li>
      <li> Inverse in Modulo </li>
    </ol>
  </li>
</ul>

<h2 id="py"> Python Installation </h2>
<p>
  If you are new to Python, then here's some steps you could follow to get started with setting it up on your PC.
  <br>
  Short path to get Python on your PC is to download < a href="https://thonny.org/">Thonny</a>. This is really a beginner friendly IDE. Python is attached with Thonny, so once you have Thonny on your PC, you can run any .py program on it.
  <br>
  To my Linux friends, the following commands can install Thonny/Python on your device:
  <br>
  <dl>
    <dt>
  <em>Raspbian</em>
    </dt>
  <dd>
    
  ```
  sudo apt install thonny
  ```
    
  </dd>
  <dt>
    <em>Debian</em>
    </dt>
  <dd>
    
  ```
  sudo apt install python3-tk thonny
  ```
    
  </dd>
  <dt>
    <em>Ubuntu</em>
  </dt>
  <dd>
    
  ```
  sudo apt install python3-tk thonny
  ```
    
  </dd>
  <dt>
    <em>Fedora</em>
  </dt>
  <dd>
    
  ```
  sudo dnf install python3-tkinter thonny
  ```
    
  </dd>
    
 </dl>
<i> Keke... Now we should be ready to jumpy into the pool of Python and RSA :D</i>
<p align="right"><a href="#gd">↑Top</a></p>
</p>

<h2 id="menu"> Menu </h2>
In this chapter, I am going to explain to you the two main functions of this program. Before that, let me introduce you two best friends: <em>Alice👧</em> and <em>Bob👦</em>.
<br>
Bob sometimes tells Alice little <em>secretes</em>, and he obviously <strong>doesn't want</strong> anyone else to know what those secrets are. Therefore, Bob invented an encoding method. He would first encrypted the secret, which is in English and may contain some puncutation marks, into <em>a list of inegers</em> and send it and some <strong>private and public keys</strong> to Alice. The keys are going to help Alice to decrypt that integer list back to human readable languages. <i>(Notice, even if other people know what the public key is, he/she won't be able to decrypt the message. If that person has all the keys, the decryption still cannot be done without the knowledge of RSA.)</i>

<h3> Bob 👦</h3>
<p>
  To be 
</p>
