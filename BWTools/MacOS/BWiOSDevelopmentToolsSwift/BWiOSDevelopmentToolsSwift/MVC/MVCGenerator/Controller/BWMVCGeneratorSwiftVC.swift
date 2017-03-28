//
//  BWMVCGeneratorSwiftVC.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 2017/3/23.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa

class BWMVCGeneratorSwiftVC: NSViewController {

    // MARK: UI
    // --------------- Source ---------------
    @IBOutlet weak var copyrightTextField: NSTextField!
    @IBOutlet weak var projectTextField: NSTextField!
    @IBOutlet weak var authorTextField: NSTextField!
    @IBOutlet weak var prefixTextField: NSTextField!
    @IBOutlet weak var importFileTextField: NSTextField!
    @IBOutlet weak var basicVCTextField: NSTextField!
    @IBOutlet weak var moduleTextField: NSTextField!
    @IBOutlet weak var propertyTextField: NSScrollView!
    
    // --------------- Generation ---------------
    @IBOutlet weak var svGeneration: NSScrollView!
    
    // MARK: View Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Read data from cache
        let userDefaults = UserDefaults.standard
        if let copyRight = userDefaults.value(forKey: kCopyRight) { copyrightTextField.stringValue = copyRight as! String }
        if let project = userDefaults.value(forKey: kProject) { projectTextField.stringValue = project as! String }
        if let author = userDefaults.value(forKey: kAuthor) { authorTextField.stringValue = author as! String }
        if let prefix = userDefaults.value(forKey: kPrefix) { prefixTextField.stringValue = prefix as! String }
        if let importFile = userDefaults.value(forKey: kImportFile) { importFileTextField.stringValue = importFile as! String }
        if let basicVC = userDefaults.value(forKey: kBasicVC) { basicVCTextField.stringValue = basicVC as! String}
        if let module = userDefaults.value(forKey: kModule) { moduleTextField.stringValue = module as! String }
    }
    
    // MARK: Action
    @IBAction func btnActionReset(_ sender: Any) {
        tvMVCSource.string = ""
    }
    
    @IBAction func btnActionGenerate(_ sender: Any)
    {
        // Get value
        let copyRight = NSString(string: copyrightTextField.stringValue).length > 0 ? copyrightTextField.stringValue : "BobWongStudio"
        let projectName = NSString(string: projectTextField.stringValue).length > 0 ? projectTextField.stringValue : "BWProject"
        let authorName = NSString(string: authorTextField.stringValue).length > 0 ? authorTextField.stringValue : "BobWong"
        let prefixName = NSString(string: prefixTextField.stringValue).length > 0 ? prefixTextField.stringValue : "BW"
        let importFile = NSString(string: importFileTextField.stringValue).length > 0 ? importFileTextField.stringValue : "#import <UIKit/UIKit.h>"
        let basicVC = NSString(string: basicVCTextField.stringValue).length > 0 ? basicVCTextField.stringValue : "UIViewController"
        let moduleName = NSString(string: moduleTextField.stringValue).length > 0 ? moduleTextField.stringValue : "MVC"
        
        // Write data to cache
        let userDefaults = UserDefaults.standard
        userDefaults.setValue(copyRight, forKey: kCopyRight)
        userDefaults.setValue(projectName, forKey: kProject)
        userDefaults.setValue(authorName, forKey: kAuthor)
        userDefaults.setValue(prefixName, forKey: kPrefix)
        userDefaults.setValue(importFile, forKey: kImportFile)
        userDefaults.setValue(basicVC, forKey: kBasicVC)
        userDefaults.setValue(moduleName, forKey: kModule)
        
        // Generate code
    }
    
    // MARK: Getter and Setter
    var tvMVCSource: NSTextView {
        get { return propertyTextField.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
    
}
