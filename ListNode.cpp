//链表的创建，插入和量长

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<stack>

using namespace std;
template<class T>
struct BSNode
{
	T value	;
	BSNode<T> *parent, *lnode, *rnode;
	BSNode(T t) :value(t), lchild(nullptr), rchild(nullptr){}
	BSNode() = default;
};

typedef struct stu{
	int age;
	stu * next;
};

void createListNode(stu * pHead){
	stu * p = pHead;
	for(int i=0;i<10;i++){
		stu * pNewNode = new stu;
		pNewNode->age = 20 + i;
		pNewNode->next = NULL;
		p->next = pNewNode;
		p = pNewNode;
	}
}

void insertListNode(stu *pHead,stu *insertNode){
	insertNode->next=pHead->next;
	pHead->next = insertNode;
}

int measure(stu *pHead){
	int length = 0;
	stu *test = pHead;
	while (test->next != NULL) {
		length++;
		test = test->next;
	}
	return length;
}
int main() {
	stu * head = NULL;
	head = new stu;
	head->age = 19;
	head->next = NULL;
	createListNode(head);
	int length = 0;
	stu *insertNode = new stu;
	insertNode->age = 45;
	insertNode->next = NULL;
	insertListNode(head, insertNode);
	for(stu *point=head;point;point=point->next){
		cout << point->age << endl;
	}
	delete head;
	return 0;
}
