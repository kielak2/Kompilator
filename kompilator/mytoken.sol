pragma solidity ^0.8.6;

contract MyContract {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 8;
    uint256 public totalSupply;

    mapping(address => uint256) balances;
    mapping(address => mapping (address => uint256)) allowed;

    constructor(uint256 _totalSupply) public {
        totalSupply = _totalSupply;
        balances[msg.sender] = _totalSupply;   
    }

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    function transfer(address receiver, uint256 numTokens) public returns (bool) {
        require(numTokens <= balances[msg.sender]);
        balances[msg.sender] -= numTokens;
        balances[receiver] = balances[receiver] + numTokens;
        emit Transfer(msg.sender, receiver, numTokens);
        return true;
    }

    function approve(address delegate, uint256 numTokens) public returns (bool) {
        allowed[msg.sender][delegate] = numTokens;
        emit Approval(msg.sender, delegate, numTokens);
        return true;
    }
    
    function allowance(address owner, address delegate) public view returns (uint) {
        return allowed[owner][delegate];
    }

    function transferFrom(address owner, address buyer, uint256 numTokens) public returns (bool) {
        require(numTokens <= balances[owner]);
        require(numTokens <= allowed[owner][msg.sender]);
        balances[owner] -= numTokens;
        allowed[owner][msg.sender] = allowed[buyer][msg.sender] - numTokens;
        balances[buyer] = balances[buyer] + numTokens;
        transfer(owner, buyer, numTokens);
        return true;
    }

   
    

}
