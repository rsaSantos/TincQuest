// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;


// Event contract
// This contract is used to store the event details such as
//  - Organizer
//  - Prize pool
//  - Participants
contract Event {
    
    // Organizer of the event: funds the prize pool and decides the winner
    address payable public organizer;

    // Prize pool of the event: funded by organizer and excess funds from enrollment fees
    uint256 public prizePool;

    // Participants of the event: addresses of non-organizer that send the enrollment fee
    address[] public participants;

    // Entry fee of the event: amount of ETH that participants must send to enroll
    uint256 public entryFee;

    // Minimum prize pool: minimum amount of ETH that must be in the prize pool to start the event
    uint256 public minimumPrizePool;

    // Percentage of the entry fee that goes to the prize pool
    uint256 public enrollToPrizePoolPercentage;

    // Values in the constructor are in wei!
    constructor(
        uint256 _entryFee,
        uint256 _minimumPrizePool,
        uint256 _enrollToPrizePoolPercentage
    ) payable
    {
        require(msg.value >= _minimumPrizePool, "Minimum prize pool must be funded.");
        require(_entryFee >= 0, "Entry fee must be greater or equal than 0.");
        require(_minimumPrizePool > 0, "Minimum prize pool must be greater than 0.");
        require(_enrollToPrizePoolPercentage >= 0 && _enrollToPrizePoolPercentage <= 100, "Enroll to prize pool percentage must be between 0 and 100.");
        
        organizer = payable(msg.sender);
        entryFee = _entryFee;
        minimumPrizePool = _minimumPrizePool;
        enrollToPrizePoolPercentage = _enrollToPrizePoolPercentage;
        prizePool = msg.value;
    }

    // Modifier to check if the organizer is the caller
    modifier onlyOrganizer() 
    {
        require(msg.sender == organizer, "Only organizer can call this function.");
        _;
    }

    // Enroll in the event (anyone unless the organizer can call this function)
    function enroll() public payable 
    {
        require(msg.sender != organizer, "Organizer cannot enroll.");
        require(msg.value >= entryFee, "Insufficient entry fee.");
        require(!isParticipant(msg.sender), "Address already enrolled.");

        if (msg.value >= entryFee) {
            // Add excess funds to the prize pool
            prizePool += (msg.value - entryFee);

            // Add participant to the list of participants
            participants.push(msg.sender);

            // Add entry fee to the prize pool (respecting the percentage)
            prizePool += (entryFee * enrollToPrizePoolPercentage) / 100;
        }
    }

    // Get the sum of an array of uint256
    function getSum(uint256[] memory arr) private pure returns (uint256) 
    {
        uint256 sum = 0;
        for (uint256 i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum;
    }

    // Terminate the event (only organizer can call this function)
    // Distribute the prize pool to the winner (or winners)
    // Send the remaining funds to the organizer
    function terminate(
        address payable[] memory winners,
        uint256[] memory prizeShare
    ) public onlyOrganizer
    {
        require(winners.length == prizeShare.length, "Number of winners and prize shares must be equal.");
        require(winners.length > 0, "At least one winner must be specified.");
        require(getSum(prizeShare) == 100, "Sum of prize shares must be 100.");

        // Distribute the prize pool to the winners
        for (uint256 i = 0; i < winners.length; i++) {
            winners[i].transfer((prizePool * prizeShare[i]) / 100);
        }

        // Send the remaining funds to the organizer
        organizer.transfer(address(this).balance);

        // Reset the prize pool
        prizePool = 0;
    }

    // Check if an address is a participant
    function isParticipant(address addr) public view returns (bool) 
    {
        for (uint256 i = 0; i < participants.length; i++) {
            if (participants[i] == addr) {
                return true;
            }
        }
        return false;
    }

    // Get number of participants
    function getNumberOfParticipants() public view returns (uint256) 
    {
        return participants.length;
    }

}
