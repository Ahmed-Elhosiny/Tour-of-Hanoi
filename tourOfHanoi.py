def prnt( disk, source, destination):
  print(f"{hanoi.steps} Disk {disk} moves from tower {source} to tower {destination}.")
  hanoi.steps += 1

def hanoi(disks, source, helper, destination ):
  if(disks == 1):
    prnt(disks, source, destination)
    return
  
  hanoi(disks - 1, source, destination, helper )
  prnt(disks, source, destination)
  hanoi(disks - 1, helper, source, destination)

disks = int(input('Number of disks to be displaced: '))
hanoi.steps = 1
hanoi(disks, 'A', 'B', 'C')

print(f"Total steps: {hanoi.steps - 1}")
print(f"Total steps: {2 ** disks - 1}")