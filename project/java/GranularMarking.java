package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  A granular marking is a grouping of characteristics unique to specification of MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared) that apply to particular portions of a particular UCO object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GranularMarking extends UcoInherentCharacterizationThing {

  private List<String> marking;
  private List<String> contentSelectors;

}