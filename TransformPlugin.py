import sys
import numpy
import math
class TransformPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = float(contents[j+1])
               self.ADJ[i][j] = value
            i += 1

      # Sum of each row
      self.rowsums = []
      for i in range(self.m):
         self.rowsums.append(0)
         for j in range(self.n):
            self.rowsums[i] += self.ADJ[i][j]

      # Geometric mean of each column
      self.geomeans = []
      for j in range(self.n):
         self.geomeans.append(1)
         for i in range(self.m):
            self.geomeans[j] *= (self.ADJ[i][j]+1)
         self.geomeans[j] = math.pow(self.geomeans[j], 1./self.m)

      # Euclidean mean of each column
      self.eucmeans = []
      for j in range(self.n):
         self.eucmeans.append(0)
         for i in range(self.m):
            self.eucmeans[j] += (self.ADJ[i][j]/self.rowsums[i])*(self.ADJ[i][j]/self.rowsums[i])
         self.eucmeans[j] = math.sqrt(self.eucmeans[j])
         if (self.eucmeans[j] == 0):
            print("WARNING: OTU "+self.bacteria[j]+" IS ZERO IN ALL SAMPLES.")


   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline)
      for i in range(self.m):
         #sum = float(0.0)
         #for j in range(self.n):
         #   sum += self.ADJ[i][j]
         for j in range(self.n):
            #print "DIVIDING ", self.ADJ[i][j], " BY: ", self.rowsums[i]*self.geomeans[j]*self.eucmeans[j], "INDIVIDUAL: ", self.rowsums[i], self.geomeans[j], self.eucmeans[j]
            self.ADJ[i][j] /= (self.rowsums[i]*self.geomeans[j]*self.eucmeans[j])
            
      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



