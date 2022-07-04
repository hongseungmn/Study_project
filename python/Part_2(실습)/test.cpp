#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(int x) {
    int a = x%10;
    int b = int(x/10);
    
    bool answer = true;
    
    if(x%(b+a)==0)
    {
        
    }
    else
        answer = false;
    
    return answer;
}

int main()
{
    cout<<solution(22)<<endl;
}