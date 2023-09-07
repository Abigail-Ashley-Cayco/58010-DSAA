#include<iostream>
using namespace std;
int main()
{
	int num[] = {1,2,3,4,5,6,7,8,9,10};
	int append = 11;
	int size = sizeof(num)/sizeof(num[0]);
	cout<<"Original Array: ";
	for(int i = 0; i<size;i++)
	{
		cout<<num[i]<<" ";
	}
	num[size]=append;
	
	cout<<endl<<"New Array: ";
	for(int i = 0; i<=size;i++)
	{
		cout<<num[i]<<" ";
	}
	return 0;
}
