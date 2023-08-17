<head>
  <div align=corner>
    <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/993782dbef600360a61a4393555f3afc0e3c61b1/icons/Python-Dark.svg" width="30px">
  </div>
    <div align=center>
    <img src="https://cdn-icons-png.flaticon.com/512/3367/3367465.png" width=200px> 
    <h1>Connect Four in Python</h1>
    <img align=right src="http://img.shields.io/static/v1?label=STATUS&message=COMPLETED&color=GREEN&style=for-the-badge" width="145px"/>
  </div>
</head>
  
<body>

  ## Description
  This is an implementation of the classic Connect Four game in Python, emphasizing the use of Object-Oriented Programming (OOP) principles.
    
  ## Features
  - Two-player mode: Human vs. Human.
  - Single-player mode: Human vs. Computer (computer makes random, but valid, moves).
  - Text-based UI with clear game state display and interaction prompts.
  
  ## Setup & Usage
  1. Prerequisites: Ensure you have Python (version 3.7 or later) installed on your machine.
  2. Clone the Repository:
    <pre>
      git clone (https://github.com/micapareddes/connect-four.git)
    </pre>
  3. Navigate to the location where you've downloaded or cloned the file.
  4. Run the Game:
     <pre>
       python connect_four.py
     </pre>

  6. Follow on-screen prompts to play game.
  
  ## Game Rules
  - Players take turns to drop a disc into one of the seven columns.
  - The aim is to be the first to connect four of one's discs in a row, either vertically, horizontally, or diagonally.
  - If the board fills up before either player achieves this, the game is a draw.
  
  ## Known Issues
  1. The game starts immediately upon script execution. It could benefit from a menu or start option.
  2. Some parts of the code contain commented-out blocks which should be cleaned up for clarity.
  3. The computer's moves are entirely random. This could make it relatively easy for an experienced player to win against the computer.
  ## Future Enhancements
  1. A visual interface will be added using the Pygame library.
  2. Implement a smarter AI opponent that uses strategies to block the player and create its winning paths.
  3. Optimize the algorithms for checking win conditions, potentially using more efficient techniques.
  
  ## Contributing
 If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcomed.

 ## Note 
 This was my initial attempt at applying Object-Oriented Programming (OOP). While the basics of OOP were implemented, there's room for improvement and optimization in the architecture.

</body>
