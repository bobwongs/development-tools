//
//  BWAPIManagerGeneratorVC.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 2017/1/18.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa

class BWAPIManagerGeneratorVC: NSViewController {

    // MARK: UI
    @IBOutlet weak var svSource: NSScrollView!
    @IBOutlet weak var svGeneration: NSScrollView!
    
    // MARK: View Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do view setup here.
    }
    
    // MARK: Action
    @IBAction func btnActReset(_ sender: Any) {
    }
    
    @IBAction func btnActGenerate(_ sender: Any) {
    }
    
    // MARK: Getter and Setter
    var tvSource: NSTextView {
        get { return svSource.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
}
