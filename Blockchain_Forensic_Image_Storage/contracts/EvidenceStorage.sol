pragma solidity ^0.8.0;

contract EvidenceStorage {

    struct Evidence {
        string hash;
        string filename;
        string user;
        string timestamp;
    }

    mapping(string => Evidence) public evidences;

    function storeEvidence(
        string memory _hash,
        string memory _filename,
        string memory _user,
        string memory _time
    ) public {
        evidences[_filename] = Evidence(_hash, _filename, _user, _time);
    }

    function getEvidence(string memory _filename) public view returns (
        string memory, string memory, string memory, string memory
    ) {
        Evidence memory e = evidences[_filename];
        return (e.hash, e.filename, e.user, e.timestamp);
    }
}