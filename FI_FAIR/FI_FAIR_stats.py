import json

def repFeatsPerSource(instances, outfile, S):
    stats1 = open(outfile,'w')
    stats1.write('instances\tfeature\tsource\n')

    for i in range(6):
        f = {}
        f['name'] = 0
        f['source'] = S[i]
        f['description'] = 0
        f['version'] = 0
        f['type_'] = 0
        f['links'] =0
        f['publication'] = 0
        f['download'] = 0
        f['inst_instr'] = 0
        f['test'] = 0
        f['src'] = 0
        f['os'] = 0
        f['input_'] = 0
        f['output'] = 0
        f['dependencies'] = 0
        f['documentation'] = 0
        f['license'] = 0
        f['termsUse'] = 0
        f['contribPolicy'] = 0
        f['authors'] = 0
        f['repository'] = 0
        f['description'] = 0

        for inst in f['source']:
            if inst.name != None:
                f['name'] += 1

            if inst.version and len(inst.version)>0:
                f['version'] += 1

            if inst.type and len(inst.type)>0:
                f['type_'] += 1

            if inst.links and len(inst.links)>0:
                f['links'] += 1

            if inst.publication>0:
                f['publication'] += 1

            if inst.download and len(inst.download)>0:
                f['download'] += 1

            if inst.inst_instr:
                f['inst_instr'] += 1

            if inst.test != False:
                f['test'] += 1

            if inst.src and len(inst.src)>0:
                f['src'] += 1

            if inst.os and len(inst.os)>0:
                f['os'] += 1

            if inst.input and len(inst.input)>0:
                f['input_'] += 1

            if inst.output and len(inst.output)>0:
                f['output'] += 1

            if inst.dependencies and len(inst.dependencies)>0:
                f['dependencies'] += 1

            if inst.documentation and len(inst.documentation)>0:
                f['documentation'] += 1

            if inst.license and len(inst.license)>0:
                #print(inst.license)
                f['license'] += 1

            if inst.authors and len(inst.authors)>0:
                f['authors'] += 1

            if inst.repository and len(inst.repository)>0:
                f['repository'] += 1

            if inst.description and len(inst.description)>0:
                f['description'] += 1

            if inst.termsUse and len(inst.termsUse)>0:
                f['termsUse'] += 1

            if inst.contribPolicy and len(inst.contribPolicy)>0:
                f['contribPolicy'] += 1


        for feat in f.keys():
            sour = inst.source[0]
            if i==0:
                sour = 'total'
            if feat != 'source':
                stats1.write('%d\t%s\t%s\n'%(f[feat], feat, sour))

    stats1.close()


def repSourcesPerInstance(instances, outfile):
    stats2 = open(outfile, 'w')

    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    stats2.write('1\t2\t3\t>3\n'%())
    # the following dictionary may lack some combinations, it may crash. Add them if necessary
    sourcesS = {'1': {'bioagents': 0, 'bioconductor': 0, 'bioconda': 0, "galaxyShed":  0, 'galaxyConfig':0}, '2':{'GcGs': 0, 'GsBcda': 0, 'BtBcda' : 0, 'BtGc':0, 'BdaGs': 0}, '3':{ 'GsGcBcda':0}, '>3':{'all':0}}

    for inst in instances:
        if len(inst.source)==1:
            sourcesS['1'][inst.source[0]] += 1
            m1+=1
        if len(inst.source)==2:
            if set(inst.source) == set(['galaxyConfig', 'galaxyShed']):
                sourcesS['2']['GcGs'] += 1
            if set(inst.source) == set(['galaxyShed', 'bioconda']):
                sourcesS['2']['GsBcda'] += 1
            if set(inst.source) == set(['bioagents', 'bioconda']):
                sourcesS['2']['BtBcda'] +=1
            if set(inst.source) == set(['bioagents', 'galaxyConfig']):
                sourcesS['2']['BtGc'] +=1
            if set(inst.source) == set(['bioconda', 'galaxyShed']):
                sourcesS['2']['BdaGs'] +=1

            m2+=1
        if len(inst.source)==3:
            if set(inst.source) == set(['galaxyConfig', 'galaxyShed', 'bioconda']):
                 sourcesS['3']['GsGcBcda'] += 1
            m3+=1
        if len(inst.source)>3:
            m4+=1
            sourcesS['>3']['all'] += 1

    stats2.write('%d\t%d\t%d\t%d\t'%(m1, m2, m3, m4))
    stats2.close()


def repTypesPerCanon(instances, outfile, canonicalMerged):
    #outf = open(outfile, 'w')
    TTs = {'1':0,'2':0, '3':0, '4':0, '5':0, '>5':0}
    for can in canonicalMerged.canonicals:
        tps = 0
        seentys = []
        for inst in can.instances:
            if inst.type not in seentys:
                tps += 1
                seentys.append(inst.type)
        if tps<6:
            TTs[str(tps)]+=1
        else:
            TTs['>5'] += 1


def typesInInstances(instances, outfile):
    types = {}
    for inst in instances:
        if inst.type not in types.keys():
            types[inst.type]=1
        else:
            types[inst.type] += 1

    stats3 = open(outfile, 'w')
    for key in types.keys():
        stats3.write('%s\t%d\n'%(key, types[key]))
    stats3.close()


def featuresInCanonicals(instances, outfile, canonicalMerged):
    stats4 = open(outfile,'w')
    stats4.write('canonical\tname\tversion\ttype\tdescription\tlinks\tpublication\tdownload\tinst_instr\ttest\tsrc\tos\tinput_\toutput\tdependencies\tdocumentation\tlicense\ttermsUse\tcontribPolicy\tauthors\trepository\n')

    name = 0
    for can in canonicalMerged.canonicals:
        name = 0
        description = 0
        version = 0
        type_ = 0
        links =0
        publication = 0
        download = 0
        inst_instr = 0
        test = 0
        src = 0
        os = 0
        input_ = 0
        output = 0
        dependencies = 0
        documentation = 0
        license = 0
        termsUse = 0
        contribPolicy = 0
        authors = 0
        repository = 0
        description = 0

        for inst in can.instances:
            if inst.name != None:
                name += 1

            if inst.version and len(inst.version)>0:
                version += 1

            if inst.type and len(inst.type)>0:
                type_ += 1

            if inst.links and len(inst.links)>0:
                links += 1

            if inst.publication>0:
                publication += 1

            if inst.download and len(inst.download)>0:
                download += 1

            if inst.inst_instr:
                inst_instr += 1

            if inst.test != False:
                test += 1

            if inst.src and len(inst.src)>0:
                src += 1

            if inst.os and len(inst.os)>0:
                os += 1

            if inst.input and len(inst.input)>0:
                input_ += 1

            if inst.output and len(inst.output)>0:
                output += 1

            if inst.dependencies and len(inst.dependencies)>0:
                dependencies += 1

            if inst.documentation and len(inst.documentation)>0:
                documentation += 1

            if inst.license and len(inst.license)>0:
                license += 1

            if inst.termsUse and len(inst.termsUse)>0:
                termsUse += 1

            if inst.contribPolicy and len(inst.contribPolicy)>0:
                contribPolicy += 1

            if inst.authors and len(inst.authors)>0:
                authors += 1

            if inst.repository and len(inst.repository)>0:
                repository += 1

            if inst.description and len(inst.description)>0:
                description += 1

        stats4.write('%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n'%(inst.name, name, version,type_, description, links, publication, download, inst_instr, test, src, os, input_, output, dependencies, documentation, license, termsUse, contribPolicy, authors, repository))

    stats4.close()



def versionsCanon(instances, outfile, canonicalMerged):
    Vs = {'1':0,'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    for can in canonicalMerged.canonicals:
        vrs = 0
        seenvrs = []
        for inst in can.instances:
            if inst.version and inst.version not in seenvrs:
                vrs += 1
                seenvrs.append(inst.version)
        #if vrs>10:
            #print(can.name)
            #print(vrs)
        if str(vrs) not in Vs.keys():
            Vs[str(vrs)] = 1
        else:
            Vs[str(vrs)]+= 1

    stats5 = open(outfile, 'w')
    row = '%s\t%d\n'
    for nVer in Vs.keys():
        stats5.write(row%(nVer, Vs[nVer]))

    stats5.close()


def typesVersions(instances, outfile):
    Vss = {'x.x':0,'other':0, 'None':0}
    other = []
    for i in instances:
        if i.version == None:
            Vss['None'] += 1
        elif len(i.version)==1 or i.version  == 'v1':
            Vss['x.x'] += 1
        elif len(i.version.split('.'))==2:
            Vss['x.x'] += 1
        else:
            Vss['other'] += 1
            if i.version not in other:
                other.append(i.version)

    stat_ver = open(outfile, 'w')
    row = '%s\t%d\n'
    for ver in Vss.keys():
        stat_ver.write(row%(ver, Vss[ver]))

    stat_ver.close()


def typesLicenses(instances, outfile):
    Ls = {'GPL':0, 'AGPL': 0, 'artistic':0, 'MIT':0, 'apache': 0, 'LGPL':0, 'other':0, 'None':0 , 'BSD':0, 'CC':0, 'CeCILL':0}
    otherL = []
    for i in instances:
        if i.license and len(i.license)>0:
            for a in i.license:
                #print(a)
                if a == None:
                    Ls['None'] += 1
                elif a == False:
                    Ls['None'] += 1
                elif 'unlicensed' in a.lower() or 'unknown' in a.lower() or 'unlicense' in a.lower():
                    Ls['None'] += 1
                elif 'AGPL' in a or 'affero' in a.lower():
                    Ls['AGPL'] += 1
                elif 'LGPL' in a:
                    Ls['LGPL'] += 1
                elif 'GPL' in a or 'gnu' in a.lower():
                    Ls['GPL'] += 1
                elif 'artistic' in a.lower():
                    Ls['artistic'] += 1
                elif 'MIT' in a:
                    Ls['MIT'] += 1
                elif 'apache' in a.lower():
                    Ls['apache'] += 1
                elif 'BSD' in a:
                    Ls['BSD'] += 1
                elif 'CC' in a or 'creative commons' in a.lower():
                    Ls['CC'] += 1
                elif 'cecill' in a.lower():
                    Ls['CeCILL'] += 1
                else:
                    Ls['other'] +=1
                    if a not in otherL:
                        otherL.append(a)
        else:
            Ls['None'] += 1

    stat_lic= open(outfile, 'w')
    row = '%s\t%d\n'
    for lic in Ls.keys():
        stat_lic.write(row%(lic, Ls[lic]))

    stat_lic.close()

def typeLis(a):
    if a == None or a==False or 'Unlicensed' in a or 'unknown' in a.lower() or 'unlicense' in a.lower():
        return('None')
    elif 'AGPL' in a or 'affero' in a.lower():
        return('AGPL')
    elif 'LGPL' in a:
        return('LGPL')
    elif 'GPL' in a or 'gnu' in a.lower():
        return('GPL')
    elif 'artistic' in a.lower():
        return('artistic')
    elif 'MIT' in a:
        return('MIT')
    elif 'apache' in a.lower():
        return('apache')
    elif 'BSD' in a:
        return('BSD')
    elif 'CC' in a or 'creative commons' in a.lower():
        return('CC')
    elif 'cecill' in a.lower():
        return('CeCILL')
    else:
        return('other')

def diffLicenses(instances, outfile, canonicalMerged):
    LLs = {'unique':0, 'co':0,'in':0, 'None':0}
    N = 0
    M =0
    for can in canonicalMerged.canonicals:
        ls = 0
        Ls = 0
        seenls = []
        for inst in can.instances:
            #print(inst.license)
            for l in inst.license:
                #print(l)
                if l != None and l != False:
                    N += 1
                    lic = typeLis(l)
                    if lic not in seenls:
                        ls = ls + 1
                        #print(ls)
                        seenls.append(lic)
                        #print(seenls)

                    else:
                        #print('here')
                        Ls = Ls + 1
                else:
                    M+=1
                    continue

        if ls == 0:
            LLs['None'] += 1

        elif ls>1:
            LLs['in'] += 1

        elif ls == 1 and Ls>0:
            LLs['co'] += 1

        elif ls == 1 and Ls == 0:
            LLs['unique'] += 1

    stat_diffLic= open(outfile, 'w')
    row = '%s\t%d\n'
    for lic in LLs.keys():
        stat_diffLic.write(row%(lic, LLs[lic]))

    stat_diffLic.close()


from pandas import DataFrame

def dfFeatures(file):
    dtaf = open(file, 'r')
    rows = []
    c=0
    for line in dtaf:
        a = line.split('\t')[:-1]
        if c!=0:
            s = [int(a[0]), a[1], line.split('\t')[-1].split('\n')[0]]
            rows.append(s)
        else:
            a.append(line.split('\t')[-1].split('\n')[0])
            header = a
        c+=1
    df = DataFrame(rows, columns = header)
    return(df)

import numpy as np
import matplotlib as mpl
def featuresBarPlot(datFrame, outname):
    import seaborn as sns
    import matplotlib.pyplot as plt
    f, ax = plt.subplots(figsize=(15, 15))
    #sns.set_color_codes("pastel")
    sns.barplot(y="feature", x="instances", hue="source",data=datFrame)
    ax.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
    ax.yaxis.grid(False) # I olny want the vertical grid
    ax.set_axisbelow(True)
    ax.xaxis.grid(b=True, which='major', color='lightgrey', linewidth=1.0)
    ax.xaxis.grid(b=True, which='minor', color='lightgrey', linewidth=0.5)
    f.savefig(outname, bbox_inches='tight')



def dfNSources(file):
    dtaf = open(file, 'r')
    rows = []
    c=0
    for line in dtaf:
        a = line.split('\t')[:-1]
        if c!=0:
            s = [int(a[i]) for i in range(len(a))]
            rows.append(s)
        else:
            a.append(line.split('\t')[-1].split('\n')[0])
            header = a
        c+=1
    df = DataFrame(rows, columns = header)
    return(df)


def nSourcesBarPlot(datFrame, outname):
    import seaborn as sns
    import matplotlib.pyplot as plt
    f, ax = plt.subplots(figsize=(10, 4))
    #sns.set_color_codes("pastel")
    g = sns.barplot(data=datFrame)
    g.set(ylim=(0, 3700))
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()),
            fontsize=12, color='black', ha='center', va='bottom')
    f.savefig(outname, bbox_inches='tight')

def pie(df, fname):
    import matplotlib.pyplot as plt
    values = df.values[0]
    labs = df.columns.values.tolist()
    f, ax = plt.subplots(figsize=(10, 4))
    plt.pie(values, labels = labs)
    plt.tight_layout()
    p=plt.gcf()
    my_circle=plt.Circle( (0,0), 0.5, color='white')
    p.gca().add_artist(my_circle)

    f.savefig(fname, bbox_inches='tight')

def pieF(df, fname):
    import matplotlib.pyplot as plt
    values = df['value'].tolist()
    labs = df['type'].tolist()
    f, ax = plt.subplots(figsize=(10, 4))
    plt.pie(values, labels = labs, data = df)
    p=plt.gcf()
    my_circle=plt.Circle( (0,0), 0.5, color='white')
    p.gca().add_artist(my_circle)

    f.savefig(fname, bbox_inches='tight')


def dfTypes(file):
    dtaf = open(file, 'r')
    rows = []
    for line in dtaf:
        if line.strip():
            type_ = line.strip().split('\t')[0]
            value = int(line.strip().split('\t')[1])
            rows.append([type_, value])
    df = DataFrame(rows, columns = ['type', 'value'])
    return(df)

def typesBarPlot(d, outname, figsize):
    import matplotlib.pyplot as plt
    import seaborn as sns
    f, ax = plt.subplots(figsize = figsize)
    #sns.set_color_codes("pastel")
    d = d.sort_values(by="value", ascending=False)
    #print(d)
    sns.barplot(x= "value",y= "type", data = d, ci = None)
    ax.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
    ax.yaxis.grid(False) # I olny want the vertical grid
    ax.set_axisbelow(True)
    ax.xaxis.grid(b=True, which='major', color='grey', linewidth=0.7)
    ax.xaxis.grid(b=True, which='minor', color='grey', linewidth=0.2)

    f.savefig(outname, bbox_inches='tight')


def repOSystems(instances, outfile1, outfile2):
    oss = {'Linux':0,'Windows':0, 'Mac':0}
    nOs = {'0':0, '1':0, '2':0, '3':0}
    for inst in instances:
        for o in inst.os:
            oss[o] += 1
        nOs[str(len(inst.os))] += 1
    # output to file
    row = '%s\t%d\n'
    file1 = open(outfile1, 'w')
    for a in oss.keys():
        file1.write(row%(a, oss[a]))
    file1.close()

    file2 = open(outfile2, 'w')
    for e in nOs.keys():
        file2.write(row%(e, nOs[e]))
    file2.close()


def repDataformats(instances, outfile1, outfile2):
    formats = []
    specified = { 'Yes': 0 , 'No': 0}
    formats = {}
    for inst in instances:
        if len(inst.input) == 0:
            specified['No'] += 1
        else:
            specified['Yes'] += 1
            for f in inst.input:
                if 'format' in f.keys():
                    if f['format']['term'].lower().lstrip() not in formats.keys():
                        #print(f['format']['term'].lower().lstrip())
                        formats[f['format']['term'].lower().lstrip()] = 1
                    else:
                        formats[f['format']['term'].lower().lstrip()] += 1



    row = '%s\t%d\n'
    fout1 = open(outfile1, 'w')
    for a in specified.keys():
        fout1.write(row%(a, specified[a]))

    fout2 = open(outfile2, 'w')
    for a in formats.keys():
        fout2.write(row%(a, formats[a]))

    #print(specified)
    #print(formats)



def FAIRviolinPlot(infile, outname):
    import seaborn as sns
    import matplotlib.pyplot as plt
    from pandas import read_csv
    import pandas as pd
    data = read_csv(infile, sep='\t', header = None)
    data.columns = ['name', 'F', 'A', 'I', 'R', 'nSources' ,  'nTypes']
    scores = data['F'].astype(float).tolist()+data['A'].astype(float).tolist()+data['I'].astype(float).tolist()+data['R'].astype(float).tolist()
    labels = ['F']*len(data['F']) + ['A']*len(data['A'])+['I']*len(data['I'])+['R']*len(data['R'])
    #print('scores len: ' + str(len(scores)))
    #print('labels lenght: ' + str(len(labels)))
    d = {'score':scores,'principle': labels}
    dat = DataFrame(d)
    #print(dat)
    g = sns.catplot(x='principle', y= 'score' , kind="violin", data=dat)
    g.savefig(outname, bbox_inches='tight')


def computeFAIRinsts(canonicals, filename, metrics_out, scores_calc, metrics_out_path):
    F = []
    A = []
    I = []
    R = []
    names = []
    out_inst_metrics = []


    name_form = '{}/{}/{}'
    for can in canonicals.canonicals:
        for ins in can.instances:
            ins.generateFAIRMetrics()
            if  metrics_out== True:
                dic = ins.metrics.__dict__
                # name, version, type are needed to identify the instance
                dic['name'] = ins.name
                dic['type'] = ins.type
                dic['version'] = ins.version
                out_inst_metrics.append(dic)
            if scores_calc == True:
                ins.FAIRscores()
                n = name_form.format(ins.name, ins.version, ins.type)
                F.append(ins.F)
                names.append(n)
                A.append(ins.A)
                I.append(ins.I)
                R.append(ins.R)

    if metrics_out == True:
        with open(metrics_out_path, 'w') as outfile:
            json.dump(out_inst_metrics, outfile)

    if scores_calc == True:
        sF=0
        sA=0
        sI=0
        sR=0

        stats5 = open(filename, 'w')
        for i in range(len(F)):
            stats5.write('%s\t%f\t%f\t%f\t%f\t%s\t%s\n'%(names[i], F[i], A[i], I[i], R[i], 'NA', 'NA'))
            sF += F[i]
            sA += A[i]
            sI += I[i]
            sR += R[i]



        print('av_sF:%f'%(sF/len(F)))
        print('av_sA:%f'%(sA/len(A)))
        print('av_sI:%f'%(sI/len(I)))
        print('av_sR:%f'%(sR/len(R)))


def computeFAIRcanon(canonicalMerged, filename):
    Fc = []
    names = []
    Ac = []
    Ic = []
    Rc = []
    nSources = []
    nTypes = []


    for can in canonicalMerged.canonicals:
        can.computeFAIRmetrics()
        Fc.append(can.F)
        names.append(can.name)
        Ac.append(can.A)
        Ic.append(can.I)
        Rc.append(can.R)
        nSources.append((len(can.sources)))
        nTypes.append(len(can.types))

    cF=0
    cA=0
    cI=0
    cR=0

    stats6 = open(filename, 'w')
    for i in range(len(Fc)):
        stats6.write('%s\t%f\t%f\t%f\t%f\t%f\t%f\n'%(names[i], Fc[i], Ac[i], Ic[i], Rc[i], nSources[i], nTypes[i]))
        cF += Fc[i]
        cA += Ac[i]
        cI += Ic[i]
        cR += Rc[i]

    import numpy as np

    def stats(letter, cF, Fc):
        print(letter + ':\n')
        print('mean = %f'%(cF/len(canonicalMerged.canonicals)))
        print('percentiles = ')
        print(np.percentile(Fc, [25, 50, 75]))
        print('min = ' + str(min(Fc)))
        print('max = ' + str(max(Fc)))

    stats('Findability scores', cF, Fc)
    stats('Accessibility scores', cA, Ac)
    stats('Interoperability scores', cI, Ic)
    stats('Reusability scores', cR, Rc)
