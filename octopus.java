// 2021 UCF HSPT - Octopus Garden
// Author: Natalie Longtin

/*
observe that performing a cyclic shift in either direction is equivalent
to taking a single element of the array and placing it somewhere else.
our problem is then reduced to: what is the minimum number of elements
we need to move somewhere else in order to sort the array?

since it never makes sense to move the same element more than once, we just need to
choose which elements to move and which elements to keep in the same spot.
we want to leave as many in the same place as possible.

observe that this maximum value is equal to the maximum number
that are already in the correct relative order,
subtracted from the total number of elements in the array.
and so our problem is further reduced to finding the longest increasing subsequence (LIS)
of the array; the answer will be n - LIS.
*/

import java.util.Arrays;
import java.util.Scanner;

public class octopus {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		
		//process test cases
		int t=scan.nextInt();
		for(int tt=0;tt<t;tt++) {
			int n=scan.nextInt();
			int[] a=new int[n];
			for(int i=0;i<n;i++) a[i]=scan.nextInt();
			
			//lis(a) elements will already be in the correct order
			//this means that n-lis(a) elements are out of place and must be moved
			System.out.println(n-lis(a));
		}
	}
	
	//nlog(n) implementation of longest increasing subsequence
	//the principle is that we add the elements to the LIS one by one,
	//overwriting the earliest element we can each time,
	//and keeping track of the longest LIS we have encountered so far.
	
	public static int lis(int[] a) {
		int n=a.length;
		int inf=Integer.MAX_VALUE/2-5;
		int[] insert=new int[n+1];
		
		Arrays.fill(insert,inf);
		insert[0]=-inf;
		int[] lis=new int[n];
		int res=0;
		
		for(int i=0;i<n;i++) {
			int idx=search(insert,a[i]);
			insert[idx]=a[i];
			lis[i]=idx;
			res=Math.max(res,lis[i]);
		}
		return res;
	}
	
	//search(a,x) returns the smallest index such that a[i]>=x
	public static int search(int[] a, int x) {
		int res=-1;
		
		int n=a.length;
		int lo=0, hi=n-1;
		while(hi>=lo) {
			int mid=(lo+hi)/2;
			if(a[mid]>=x) {
				res=mid;
				hi=mid-1;
			}
			else lo=mid+1;
		}
		return res;
	}
}
