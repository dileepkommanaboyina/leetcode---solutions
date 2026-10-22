class Solution {
public:
    string defangIPaddr(string address) {
        string newADD;
        for(int i =0; i<address.length();i++){
            if(address[i] == '.'){
                newADD += "[.]";
            }
            else
            {
                newADD.push_back(address[i]); 
            }
        }
        return newADD;
    }

};
