import csv, sys

def main(ipv4="GeoLite2-ASN-Blocks-IPv4.csv", ipv6="GeoLite2-ASN-Blocks-IPv6.csv", output="./"):
    asnlist = []
    asndict = {}
    with open(ipv4, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            if row['autonomous_system_number'] not in asnlist:
                asndict[row['autonomous_system_number']] = [row['network']]
                asnlist.append(row['autonomous_system_number'])
            else:
                asndict[row['autonomous_system_number']].append(row['network'])
            print(row['network'],row['autonomous_system_number'])
        csvfile.close()

    with open(ipv6, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            if row['autonomous_system_number'] not in asnlist:
                asndict[row['autonomous_system_number']] = [row['network']]
                asnlist.append(row['autonomous_system_number'])
            else:
                asndict[row['autonomous_system_number']].append(row['network'])
            print(row['network'],row['autonomous_system_number'])
        csvfile.close()

    for i in asnlist:
        exportData = ""
        for j in asndict[i]:
            exportData += j + "\n"
        with open(output+"/as"+i,"w") as f:
            f.write(exportData)
            f.close()
        
if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])