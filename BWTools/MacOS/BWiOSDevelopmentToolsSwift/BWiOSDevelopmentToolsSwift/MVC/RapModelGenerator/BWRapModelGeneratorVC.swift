//
//  BWRapModelGeneratorVC.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 2017/7/12.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa

class BWRapModelGeneratorVC: NSViewController {

    // MARK: UI
    // --------------- Source ---------------
    @IBOutlet weak var tfCopyRight: NSTextField!
    @IBOutlet weak var tfProject: NSTextField!
    @IBOutlet weak var tfAuthor: NSTextField!
    @IBOutlet weak var tfPrefix: NSTextField!
    @IBOutlet weak var tfImportFile: NSTextField!
    @IBOutlet weak var tfBasicVC: NSTextField!
    @IBOutlet weak var tfModule: NSTextField!
    @IBOutlet weak var svProperty: NSScrollView!
    
    // --------------- Generation ---------------
    @IBOutlet weak var svGeneration: NSScrollView!
    
    // MARK: View Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Read data from cache
        let userDefaults = UserDefaults.standard
        if let copyRight = userDefaults.value(forKey: kCopyRight) { tfCopyRight.stringValue = copyRight as! String }
        if let project = userDefaults.value(forKey: kProject) { tfProject.stringValue = project as! String }
        if let author = userDefaults.value(forKey: kAuthor) { tfAuthor.stringValue = author as! String }
        if let prefix = userDefaults.value(forKey: kPrefix) { tfPrefix.stringValue = prefix as! String }
        if let importFile = userDefaults.value(forKey: kRapModelImportFile) { tfImportFile.stringValue = importFile as! String }
        if let basicVC = userDefaults.value(forKey: kRapModelBasic) { tfBasicVC.stringValue = basicVC as! String}
        if let module = userDefaults.value(forKey: kRapModelModule) { tfModule.stringValue = module as! String }
    }
    
    // MARK: Action
    @IBAction func btnActionReset(_ sender: Any) {
        tvSource.string = ""
    }
    
    @IBAction func btnActionGenerate(_ sender: Any)
    {
        // Set the path parameters for source and generation directory
        let source = tvSource.string
        let pathGeneratorDir = "\(NSHomeDirectory())/Desktop/Generator/RapModel"
        let pathSourceDir = "\(pathGeneratorDir)/Source"
        let pathGenerationDir = "\(pathGeneratorDir)/Generation"
        
        let pathSource = "\(pathSourceDir)/source.txt"
        let pathGeneration = "\(pathGenerationDir)/generation.txt"
        
        // If there not has file, create
        if !hasDirectory(path: pathSourceDir) { return }
        if !hasFile(path: pathSource) { return }
        
        let copyRight = NSString(string: tfCopyRight.stringValue).length > 0 ? tfCopyRight.stringValue : "BobWongStudio"
        let projectName = NSString(string: tfProject.stringValue).length > 0 ? tfProject.stringValue : "BWProject"
        let authorName = NSString(string: tfAuthor.stringValue).length > 0 ? tfAuthor.stringValue : "BobWong"
        let prefixName = NSString(string: tfPrefix.stringValue).length > 0 ? tfPrefix.stringValue : "BW"
        let importFile = NSString(string: tfImportFile.stringValue).length > 0 ? tfImportFile.stringValue : "#import <UIKit/UIKit.h>"
        let basicVC = NSString(string: tfBasicVC.stringValue).length > 0 ? tfBasicVC.stringValue : "UIViewController"
        let moduleName = NSString(string: tfModule.stringValue).length > 0 ? tfModule.stringValue : "RapModel"
        
        tvGeneration.string = executePythonScript(scriptInBundle: "generator_rap_model", sourcePath: pathSource, generationPath: pathGeneration, source: source, argumentsExceptPath: ["-c", copyRight, "-p", projectName, "-a", authorName, "-P", prefixName, "-i", importFile, "-b", basicVC, "-m", moduleName])
        
        
        // Write data to cache
        let userDefaults = UserDefaults.standard
        userDefaults.setValue(copyRight, forKey: kCopyRight)
        userDefaults.setValue(projectName, forKey: kProject)
        userDefaults.setValue(authorName, forKey: kAuthor)
        userDefaults.setValue(prefixName, forKey: kPrefix)
        userDefaults.setValue(importFile, forKey: kRapModelImportFile)
        userDefaults.setValue(basicVC, forKey: kRapModelBasic)
        userDefaults.setValue(moduleName, forKey: kRapModelModule)
    }
    
    // MARK: Getter and Setter
    var tvSource: NSTextView {
        get { return svProperty.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
    
}
