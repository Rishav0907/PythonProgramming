{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "string1=\"Hello\"\n",
    "string2=\"Morning\"\n",
    "x=string1[slice(0,2)]\n",
    "y=string2[slice(0,2)]\n",
    "z=string1[slice(3,4)]\n",
    "print(x)\n",
    "print(y)\n",
    "print(z)\n",
    "print(string2*2)\n",
    "print(string1+string2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list1=['ubuntu','fedora','kali','parrot','mint','manjaro']\n",
    "list1[3]\n",
    "print(list1*3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tup1=(('windows','linux','mac'))\n",
    "print(tup1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1={'model':'oneplus7',\n",
    "       'ram':'12gb',\n",
    "       'hdd':'512gb',\n",
    "       'battery':'4500mah'}\n",
    "\n",
    "print(dict1['model'])\n",
    "for i in dict1:\n",
    "    print(dict1[i])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=int(input(\">\"))\n",
    "if(x%2==0):\n",
    "    print(\"Even\")\n",
    "else:\n",
    "    print(\"Odd\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "> 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 * 1 = 5\n",
      "5 * 2 = 10\n",
      "5 * 3 = 15\n",
      "5 * 4 = 20\n",
      "5 * 5 = 25\n",
      "5 * 6 = 30\n",
      "5 * 7 = 35\n",
      "5 * 8 = 40\n",
      "5 * 9 = 45\n",
      "5 * 10 = 50\n"
     ]
    }
   ],
   "source": [
    "i=1\n",
    "n=int(input(\">\"))\n",
    "while(i<=10):\n",
    "    a=n*i\n",
    "    print(n,'*',i,'=',a)\n",
    "    i=i+1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def add(a,b):\n",
    "    return a+b\n",
    "add(5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "> 5\n",
      "> 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\">\"))\n",
    "y=int(input(\">\"))\n",
    "num=[x,y]\n",
    "Sum=sum(num)\n",
    "print(Sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
