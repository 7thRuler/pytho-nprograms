{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b9abf633",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square matrix\n",
      "Enter number of rows and columns: 3\n",
      "\n",
      " Enter the elements of matrix: \n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "\n",
      "Given matrix: \n",
      " [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n",
      "Dictionary is : {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}\n"
     ]
    }
   ],
   "source": [
    "a=[]\n",
    "print(\"Square matrix\")\n",
    "n=int(input(\"Enter number of rows and columns: \"))\n",
    "b={}\n",
    "a=[[]*n for i in range (n)]\n",
    "print(\"\\n Enter the elements of matrix: \")\n",
    "for i in range(0,n):\n",
    "    for j in range (0,n):\n",
    "        a[i].append(int(input()))\n",
    "print (\"\\nGiven matrix: \\n\",a)\n",
    "for i in range (0,n):\n",
    "    for j in range (0,n):\n",
    "        if a[i][j]!=0:\n",
    "              b[(i,j)]=a[i][j]\n",
    "print(\"Dictionary is :\",b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19eb80bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
