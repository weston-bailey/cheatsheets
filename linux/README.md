# Notes on Linux

## Drives, Partitions, Filesystems and Formatting

how to see all the mounted filesystems?

```bash
# this gives a definate list that is hard to read
cat /proc/mounts 
# this create a nicely readable tree
findmnt
# this shows hard disks with volume information
lsblk -f
# parted gives partition and volume information
parted -l
```


partitioning and formatting 

```bash
# start working on a partition with: 
sudo parted /dev/disk (should be disk name) consider using the -a option
# prints info about working disk
print 
# removes partitions by number
rm 2
# make a new label
mklabel gpt (or other filesystem)
# make a partition (this is where that -a gets important)
mkpart primary 0% 100% 
```

 > In order to align partition with parted you can use --align option. Valid alignment types are:

*  none - Use the minimum alignment allowed by the disk type.
*  cylinder - Align partitions to cylinders.
* minimal - Use minimum alignment as given by the disk topology information. This and the opt value will use layout information provided by the disk to align the logical partition table addresses to actual physical blocks on the disks. The min value is the minimum alignment needed to align the partition properly to physical blocks, which avoids performance degradation.
 * optimal Use optimum alignment as given by the disk topology information. This aligns to a multiple of the physical block size in a way that guarantees optimal performance.

[here](https://docs.fedoraproject.org/en-US/quick-docs/creating-a-disk-partition-in-linux/) is a link that may come in handy

## Snap

add some snap info

[good tutorial here](https://www.tecmint.com/install-snap-in-linux/)

4bit number = four places
base is number you count to

current * (place ^ base) + number

	       base ^ 3 + number
	      / base ^ 2 + number
             / / base ^ 1 + number
            / / /
           / / / 
place   =  3 2 1 0
number  =  0 1 5 3 
current =    ^ 
