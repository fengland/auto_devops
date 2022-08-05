CREATE TABLE `0_motherboard`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `serial` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE,
      INDEX `location`(`location`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `1_processor`  (
      `id` int NOT NULL,
      `serial` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE,
      INDEX `location`(`location`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `2_memory`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `serial` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      UNIQUE INDEX `serial`(`serial`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE,
      INDEX `location`(`location`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `20_motherboard_product`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `厂商` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `21_processor_productor`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `productor_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `vendor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `capacity` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `width` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `clock` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `productor_id`(`productor_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `22_memory_product`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `vendor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `size` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `width` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `clock` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `23_disk_product`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `厂商` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `硬盘容量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `接口类型` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `接口速率` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `缓存` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `硬盘尺寸` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `转速` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `内部传输速率` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `平均无故障时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `硬盘重量` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `27_power_product`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `vendor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `capacity` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `3_disk`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `serial` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE,
      INDEX `location`(`location`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `7_power`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `serial` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `product_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `product_id`(`product_id`) USING BTREE,
      INDEX `location`(`location`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `host_index`  (
      `id` int NOT NULL AUTO_INCREMENT,
      `上架日期` date NULL DEFAULT NULL,
      `地点` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `ASSETS_ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `机器状态` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `产权` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `使用节点号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `角色` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `RACK_ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `管理内网IP` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `业务IP` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `新加坡业务IP` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `ipmitool IP` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `BMC账号密码` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `机器SN` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `品牌` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `型号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `OS版本` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE,
      INDEX `ASSETS_ID`(`ASSETS_ID`) USING BTREE,
      INDEX `RACK_ID`(`RACK_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 46 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `idc_info`  (
      `ID` int NOT NULL,
      `IDC_ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `IDC_NAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `IDC_LOCATION` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `START_DATE` date NULL DEFAULT NULL,
      PRIMARY KEY (`ID`) USING BTREE,
      INDEX `IDC_ID`(`IDC_ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

CREATE TABLE `rack_info`  (
      `ID` int NOT NULL AUTO_INCREMENT,
      `RACK_ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
      `IDC_ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      `START_DATE` date NULL DEFAULT NULL,
      `PROPERTY_RIGHT` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
      PRIMARY KEY (`ID`) USING BTREE,
      INDEX `RACK_ID`(`RACK_ID`) USING BTREE,
      INDEX `IDC_ID`(`IDC_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

ALTER TABLE `0_motherboard` ADD CONSTRAINT `0_motherboard_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `20_motherboard_product` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `0_motherboard` ADD CONSTRAINT `0_motherboard_ibfk_2` FOREIGN KEY (`location`) REFERENCES `host_index` (`ASSETS_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `1_processor` ADD CONSTRAINT `1_processor_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `21_processor_productor` (`productor_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `1_processor` ADD CONSTRAINT `1_processor_ibfk_2` FOREIGN KEY (`location`) REFERENCES `host_index` (`ASSETS_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `2_memory` ADD CONSTRAINT `2_memory_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `22_memory_product` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `2_memory` ADD CONSTRAINT `2_memory_ibfk_2` FOREIGN KEY (`location`) REFERENCES `host_index` (`ASSETS_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `3_disk` ADD CONSTRAINT `3_disk_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `23_disk_product` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `3_disk` ADD CONSTRAINT `3_disk_ibfk_2` FOREIGN KEY (`location`) REFERENCES `host_index` (`ASSETS_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `7_power` ADD CONSTRAINT `7_power_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `27_power_product` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `7_power` ADD CONSTRAINT `7_power_ibfk_2` FOREIGN KEY (`location`) REFERENCES `host_index` (`ASSETS_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `host_index` ADD CONSTRAINT `host_index_ibfk_1` FOREIGN KEY (`RACK_ID`) REFERENCES `rack_info` (`RACK_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `rack_info` ADD CONSTRAINT `rack_info_ibfk_1` FOREIGN KEY (`IDC_ID`) REFERENCES `idc_info` (`IDC_ID`) ON DELETE SET NULL ON UPDATE RESTRICT;
