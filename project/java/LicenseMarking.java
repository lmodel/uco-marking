package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  A MarkingDefinition is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LicenseMarking extends MarkingModel {

  private List<String> definitionType;
  private String license;

}