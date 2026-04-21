**An Intelligent Blockchain Framework for Secure Digital Forensic Evidence Management**

**Overview**

* This project presents an intelligent blockchain-based framework for secure digital forensic evidence management. It ensures data integrity, transparency, and tamper-proof storage of digital evidence such as images using a combination of blockchain, cryptographic hashing, and decentralized storage. 
* Traditional forensic systems rely on centralized storage, making them vulnerable to manipulation and unauthorized access. This system overcomes those limitations using blockchain and IPFS integration.


**Objectives**
* Ensure tamper-proof storage of digital evidence
* Maintain a secure chain of custody
* Provide real-time verification of evidence
* Reduce manual effort using automation
* Enable transparent and auditable records

**Key Features**
* Blockchain Integration – Immutable storage of hash and metadata
* Chain of Custody Tracking – Tracks every action on evidence
* SHA-256 Hashing – Ensures data integrity
* IPFS Storage – Decentralized storage for evidence files
* Tamper Detection – Detects even minor modifications
* Automated Verification – Reduces manual validation
* Audit Logs – Transparent tracking of all activities

**System Architecture**
* User uploads digital evidence (image)
* SHA-256 generates a unique hash
* Image is stored in IPFS and generates CID
* Hash and metadata are stored on blockchain
* During verification, hash is recalculated
* Compared with blockchain hash to detect tampering

**Tech Stack**
* Language – Python, Solidity, JavaScript
* Backend – Flask
* Blockchain – Ethereum (Ganache)
* Storage – IPFS
* Blockchain Interaction – Web3.py
* Frontend – HTML, CSS, JavaScript
* Tools – VS Code

**Modules**
* User Interface Module – Interaction with users
* Image Upload Module – Handles file upload
* Hash Generation Module – Generates SHA-256 hash
* IPFS Module – Stores files in decentralized storage
* Blockchain Module – Stores hash and metadata
* Smart Contract Module – Automates transactions
* Verification Module – Checks integrity
* Audit Log Module – Maintains history

**Workflow**
* Upload image
* Generate hash
* Store image in IPFS
* Store hash in blockchain
* Verify by comparing hashes
* Output: Safe or Tampered

**Results**
* Secure storage of digital evidence
* Accurate tamper detection
* Transparent blockchain transactions
* Efficient verification process
* Login system (Investigator / Officer)
* Image upload and verification panel
* Blockchain transaction logs (Ganache)
* IPFS storage dashboard

**Applications**
* Cybercrime investigations
* Law enforcement agencies
* Digital forensic labs
* Court evidence validation
* Secure evidence sharing

**Future Scope**
* Integration with Machine Learning for classification
* Support for multiple file types (video, documents)
* Deployment on public blockchain
* Advanced analytics dashboards
* Enhanced access control and identity systems

**Conclusion**

This system provides a secure, decentralized, and reliable solution for digital evidence management. By combining blockchain, IPFS, and cryptographic hashing, it ensures integrity, transparency, and trust, making it suitable for real-world forensic applications.

**Authors**
Gauravaram Varshitha 
G.Asmitha
G.Deepika

**License**
* This project is for academic and educational purposes.


